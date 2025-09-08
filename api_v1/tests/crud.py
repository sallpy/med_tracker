
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.tests import Tests

from .schemas import TestCreate, TestUpdate, TestUpdatePartial



async def get_tests(session: AsyncSession, owner_id: int) -> list[Tests]: 
    stmt = select(Tests).where(Tests.owner_id == owner_id).order_by(Tests.id)
    result: Result = await session.execute(stmt)
    tests = result.scalars().all()
    return list(tests)


async def get_test(session: AsyncSession, test_id: int) -> Tests | None:
    return await session.get(Tests, test_id)

async def create_test(session: AsyncSession, test_in: TestCreate, owner_id: int) -> Tests:
    test = Tests(**test_in.model_dump(), owner_id=owner_id)
    session.add(test)
    await session.commit()
    #await session.refresh(test)
    return test


# put и patch - два в одном
async def update_test(session: AsyncSession, test: Tests, test_update: TestUpdate | TestUpdatePartial, partial: bool = False) -> Tests:
    for name, value in test_update.model_dump(exclude_unset=partial).items():
        setattr(test, name, value)
        await session.commit()
        return test

async def delete_test(session: AsyncSession, test: Tests):
    await session.delete(test)
    await session.commit()