from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1
from auth import get_current_active_user, router as auth_router
from models import User
# from crud import create_user

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(auth_router)


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]

# @app.post('/user')
# async def create_user(user: User):
#     return create_user(user)