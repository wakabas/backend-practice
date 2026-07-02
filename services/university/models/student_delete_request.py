from pydantic import BaseModel, ConfigDict


class StudentDeleteRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int
