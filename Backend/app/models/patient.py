from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    age: Mapped[int] = mapped_column(Integer)
    sex: Mapped[str] = mapped_column(String(1))

    chest_pain_type: Mapped[str] = mapped_column(String(10))

    resting_bp: Mapped[int] = mapped_column(Integer)

    cholesterol: Mapped[int] = mapped_column(Integer)

    fasting_bs: Mapped[int] = mapped_column(Integer)

    resting_ecg: Mapped[str] = mapped_column(String(10))

    max_hr: Mapped[int] = mapped_column(Integer)

    exercise_angina: Mapped[str] = mapped_column(String(1))

    oldpeak: Mapped[float] = mapped_column(Float)

    st_slope: Mapped[str] = mapped_column(String(10))
