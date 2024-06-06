import time
from asyncpg import DataError
from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate

router = APIRouter(prefix="/operations", tags=["operations"])


@router.get("/long_operation")
@cache(expire=30)
async def get_long_op():
    time.sleep(2)
    return "Длительная операция, которая выполняется очень долго"


# Важно лимитировать вывод из базы данных
@router.get("/")
async def get_specific_operations(
    operation_type: str, session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(Operation).where(Operation.type == operation_type).limit(2)
        result = await session.execute(query)
        return {"status": "success", "data": result.mappings().all(), "details": None}
    except DataError as exc:
        raise HTTPException(
            status_code=500, detail={"status": "error", "data": None, "detail": str(exc)}
        ) from exc
    except Exception as exc:
        # Передать ошибку разработчикам 
        raise HTTPException(
            status_code=500, detail={"status": "error", "data": None, "detail": str(exc)}
        ) from exc


# работа с post запросами / на insert запрос в БД
@router.post("/", response_description="The created data",)
async def add_specific_operations(
    new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)
):
    # stmt - Запрос на вставку. В документации так описывается (statement?))
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    # Для выполнения условия аттомарности - исполнить, например паралельно в таблицу логов добавить запись и все
    # действия были исполнены
    await session.commit()
    return {"status": "success"}

