from fastapi import APIRouter

from .tests.views import router as tests_router

router = APIRouter()
router.include_router(router=tests_router, prefix='/tests')