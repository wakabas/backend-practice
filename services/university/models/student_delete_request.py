from pydantic import BaseModel

class StudentDeleteRequest(BaseModel):
    student_id: int