from pydantic import BaseModel, Field

from services.general.models.base_grade import Grade


class GradeStatisticsResponse(BaseModel):
    count: int = Field(ge=0)
    min: int | None = Field(default=None, ge=Grade.MIN, le=Grade.MAX)
    max: int | None = Field(default=None, ge=Grade.MIN, le=Grade.MAX)
    avg: int | float | None = Field(default=None, ge=Grade.MIN, le=Grade.MAX)
