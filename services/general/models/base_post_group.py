from pydantic import BaseModel, ConfigDict


class BasePostGroup(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
