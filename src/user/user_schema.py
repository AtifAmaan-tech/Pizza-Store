
from pydantic import BaseModel, StringConstraints
from typing import Annotated, Optional

_MaxLen = 255

class Register(BaseModel):
    username: Annotated[str, StringConstraints(max_length=_MaxLen)]
    email: Annotated[str, StringConstraints(max_length=_MaxLen)]
    password: str
    is_active: Optional[bool] = None
    is_staff: Optional[bool] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "atifamaan",
                "email": "atifamaan@gmail.com",
                "password": "12345678",
                "is_active": False,
                "is_staff": True
            }
        }


class RegisterResponse(BaseModel):
    username: str
    email: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "atifamaan",
                "email": "atifamaan@gmail.com",
            }
        }
