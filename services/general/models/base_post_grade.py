from enum import IntEnum

from pydantic import BaseModel, ConfigDict, Field


class Grade(IntEnum):
    MIN = 0
    MAX = 5


class BasePostGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: Grade = Field(ge=Grade.MIN, le=Grade.MAX)
