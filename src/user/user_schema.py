
from pydantic import BaseModel, StringConstraints
from typing import Annotated, Optional

_MaxLen = 255

class Register(BaseModel):
    username: Annotated[str, StringConstraints(max_length=_MaxLen)]
    email: Annotated[str, StringConstraints(max_length=_MaxLen)]
    password: str
    is_active: Optional[bool] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "atifamaan",
                "email": "atifamaan@gmail.com",
                "password": "12345678",
                "is_active": False
            }
        }


class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "atifamaan",
                "email": "atifamaan@gmail.com",
            }
        }


class Login(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "atifamaan@gmail.com",
                "password": "12345678"
            }
        }