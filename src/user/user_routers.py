from fastapi import APIRouter, status, Depends, Request
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.user_schema import Register, UserResponse, Login
from src.user.controller import register_user, login_user, authentication, check_refresh_token


user_router = APIRouter(prefix="/user")

@user_router.post("/register",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user:Register, db:Session = Depends(get_db)):
    return await register_user(user,db)


@user_router.post('/login', status_code = status.HTTP_202_ACCEPTED)
async def login(body:Login,db:Session = Depends(get_db)):
    return await login_user(body, db)

@user_router.get("/auth",response_model = UserResponse,status_code = status.HTTP_200_OK)
async def auth(request:Request, db:Session = Depends(get_db)):
    return await authentication(request, db)

@user_router.get("/refresh",status_code=status.HTTP_200_OK)
async def refresh(requst:Request, db:Session = Depends(get_db)):
    return await check_refresh_token(requst, get_db)