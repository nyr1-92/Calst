from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ScanModel(Base):
    __tablename__ = "scans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    food_description: Mapped[str] = mapped_column(String)
    estimated_calories: Mapped[int] = mapped_column(Integer)
    min_calories: Mapped[int] = mapped_column(Integer)
    max_calories: Mapped[int] = mapped_column(Integer)
    confidence: Mapped[str] = mapped_column(String)