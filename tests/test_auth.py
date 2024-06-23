import pytest
from sqlalchemy import insert, select

from src.auth.models import Role

from .conftest import async_session_maker

@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(Role).values(id=2, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(Role)
        result = await session.execute(query)
        print(result.scalars().all())

# def test_register():
#     client.post("/auth/register", json={
#         "email": "user@example.com",
#         "password": "string",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verified": False,
#         "username": "string",
#         "role_id": 0
#     })