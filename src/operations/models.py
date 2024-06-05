from datetime import datetime
from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class Operation(Base):
    __tablename__ = "operation"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    quantity: Mapped[str] = mapped_column(String, nullable=False)
    figi: Mapped[str] = mapped_column(String, nullable=False)
    instrument_type: Mapped[str] = mapped_column(String, nullable=True)
    date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)