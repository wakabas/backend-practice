from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class Degree(StrEnum):
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DOCTORATE = "Doctorate"


class BasePostStudent(BaseModel):
    model_config =  ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    email: EmailStr
    degree: Degree
    phone: str
    group_id: int