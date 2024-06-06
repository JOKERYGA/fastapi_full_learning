from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import uvicorn
from fastapi import FastAPI
from redis import asyncio as aioredis

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserCreate, UserRead
from src.operations.router import router as router_operation


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_response=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Salary"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_operation)



if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)

# uvicorn src.main:app --reload
