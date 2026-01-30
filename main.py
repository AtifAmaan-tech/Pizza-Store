from fastapi import FastAPI
from src.user.user_routers import user_router
from src.order.order_models import OrderModel
from src.user.user_models import UserModel
from src.utils.db import Base,engine
from src.order.order_routers import order_router

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(user_router)
app.include_router(order_router)

@app.get("/")
async def read_root():
    return {"message":"Hello wooo!"}