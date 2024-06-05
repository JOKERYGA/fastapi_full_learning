from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Operation).where(Operation.type == operation_type)
    result = await session.execute(query)
    return result.mappings().all()


#работа с post запросами / на insert запрос в БД
@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    # stmt - Запрос на вставку. В документации так описывается (statement?))
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    # Для выполнения условия аттомарности - исполнить, например паралельно в таблицу логов добавить запись и все
    # действия были исполнены
    await session.commit()
    return {"status": "success"}
