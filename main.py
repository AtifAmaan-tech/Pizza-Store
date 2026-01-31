from fastapi import FastAPI
from src.user.user_routers import user_router
from src.order.order_models import OrderModel
from src.user.user_models import UserModel
from src.utils.db import Base,engine
from src.order.order_routers import order_router


app = FastAPI(
    title="Pizza Management API",
    description="API for managing users and pizza orders. Use the /user endpoints for authentication and /order endpoints to manage orders.",
    version="0.1.0",
)

Base.metadata.create_all(bind = engine)

app.include_router(user_router)
app.include_router(order_router)

@app.get("/")
async def read_root():
    """
    ### Docstring for read_root
     A simple route for getting string "Hello World!"
    """

    return {"message":"Hello World!"}