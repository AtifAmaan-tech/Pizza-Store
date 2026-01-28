from fastapi import HTTPException, status
from src.user.user_models import UserModel
from src.user.user_schema import Register
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(user:Register,db:Session):
    username = db.query(UserModel).filter(UserModel.username == user.username).first()
    if username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username already exist")

    email = db.query(UserModel).filter(UserModel.email == user.email).first()
    if email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already exist")
    
    new_user = UserModel(
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user