import sys
import uvicorn
from fastapi import FastAPI

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserCreate, UserRead
from src.operations.router import router as router_operation

sys.path.append("c:/documents/GIT/fastapi_full_learning/src")

app = FastAPI(
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


app.include_router(
    router_operation
)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)

# uvicorn src.main:app --reload
