from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "deepak",
                "email": "deepak@gmail.com",
                "password": "123",
                "year": 2,
                "gpa": "3.0",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "112",
                "year": 4,
                "gpa": "4.0",
            }
        }


