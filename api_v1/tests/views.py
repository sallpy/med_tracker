from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import TestCreate, Tests, TestUpdate, TestUpdatePartial
from .dependencies import test_by_id


router = APIRouter(tags=['test'])

@router.get('/', response_model=list[Tests])
async def get_tests(session: AsyncSession=Depends(db_helper.session_dependency)):
    return await crud.get_tests(session=session)


@router.post('/', response_model=Tests, status_code=status.HTTP_201_CREATED)
async def create_test(test_in: TestCreate, session: AsyncSession=Depends(db_helper.session_dependency)):
    return await crud.create_test(session=session, test_in=test_in)



@router.get('/{test_id}/', response_model=Tests)
async def get_test(test: Tests = Depends(test_by_id)):
    return test


@router.put('/{test_id}/')
async def update_test( test_update: TestUpdate, test: Tests = Depends(test_by_id), session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.update_test(session=session, test=test, test_update=test_update)


@router.patch('/{test_id}/')
async def update_test_partial( test_update: TestUpdatePartial, test: Tests = Depends(test_by_id), session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.update_test(session=session, test=test, test_update=test_update, partial=True)


@router.delete('/{test_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_test(test: Tests = Depends(test_by_id), session: AsyncSession = Depends(db_helper.session_dependency) ) -> None:
    await crud.delete_test(session=session, test=test)

