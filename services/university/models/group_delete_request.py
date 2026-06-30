from pydantic import BaseModel, ConfigDict


class GroupDeleteRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    group_id: int
