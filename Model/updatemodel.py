from pydantic import BaseModel,Field
from typing import Annotated , Optional


class UpdateStruct(BaseModel):
    roll:Annotated[Optional[int],Field(title="enter the roll")]
    name:Annotated[Optional[str],Field(title="enter the name")]
    age:Annotated[Optional[int],Field(title="enter the age")]


    