from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class UpdateStruct(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: Optional[str] = Field(default=None, min_length=1)
    age: Optional[int] = Field(default=None, gt=0)
    email: Optional[EmailStr] = None
