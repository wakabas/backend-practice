from pydantic import BaseModel, ConfigDict, Field


class GradeStatisticsRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int | None = Field(default=None)
    teacher_id: int | None = Field(default=None)
    group_id: int | None = Field(default=None)