from pydantic import BaseModel, ConfigDict, Field


class City(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str = Field(min_length=1)
