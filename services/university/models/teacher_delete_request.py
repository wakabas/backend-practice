from pydantic import BaseModel, ConfigDict

class TeacherDeleteRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int