from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Tests


async def test_by_id(test_id: Annotated[int, Path], session: AsyncSession=Depends(db_helper.session_dependency)) -> Tests:
    test = await crud.get_test(session=session, test_id= test_id)
    if test is not None:
        return test
    raise HTTPException(
        status_code=(status.HTTP_404_NOT_FOUND),
        detail=f'Test {test_id} not found',
    )