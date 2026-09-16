from pydantic import BaseModel,Field
from typing import Annotated


class StudentStruct(BaseModel):
    roll:Annotated[int,Field(title="enter the roll")]
    name:Annotated[str,Field(title="enter the name")]
    age:Annotated[int,Field(title="enter the age")]

    