from typing import Any

from sqlalchemy import Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseTable


class DsaQuestion(BaseTable):
    __tablename__ = "dsa_questions"

    problem_name: Mapped[str] = mapped_column(String(255), nullable=False)
    topic: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    difficulty: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    test_cases: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
    job_role: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    times_served: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return (
            f"<DsaQuestion(name='{self.problem_name}', "
            f"topic='{self.topic}', difficulty='{self.difficulty}')>"
        )
