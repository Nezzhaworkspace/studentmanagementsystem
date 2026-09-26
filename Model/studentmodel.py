from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentStruct(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    roll: int = Field(gt=0, title="Student roll number")
    name: str = Field(title="Student name", min_length=1)
    age: int = Field(title="Student age", gt=0)
    email: EmailStr = Field(title="Student email")
