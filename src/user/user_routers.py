from fastapi import APIRouter, status,Depends
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.user_schema import Register, RegisterResponse
from src.user.controller import register_user


user_router = APIRouter(prefix="/user")

@user_router.post("/register",response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(user:Register, db:Session = Depends(get_db)):
    return register_user(user,db)