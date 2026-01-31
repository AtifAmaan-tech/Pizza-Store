from fastapi import APIRouter, status, Depends
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.user_schema import UserResponse
from src.order.order_schema import OrderSchema, OrderResponse, PatchOrder,PatchOrderResponse, OrderStatusUpdate
from src.user.controller import get_current_user
from src.order.controller import place_order, get_all_orders, fetch_user_orders, fetch_specific_user_orders, patch_order,patch_order_status, remove_order


order_router = APIRouter(prefix="/order", tags=["Order"])

# Create an order
@order_router.post(
    "/create_order",
    response_model = OrderResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Create Order",
    description="Create a new pizza order for the authenticated user.",
)
async def create_order(body:OrderSchema, user:UserResponse = Depends(get_current_user),db:Session = Depends(get_db)):
    return await place_order(body,user,db)


# Get all orders [Superuser only]
@order_router.get(
    "/orders",
    summary="List All Orders",
    description="Return all orders. Restricted to staff/superuser accounts.",
)
async def get_orders(user:UserResponse = Depends(get_current_user),
db:Session = Depends(get_db)):
    return await get_all_orders(user, db)


# Get a user's all orders [Superuser only]
@order_router.get(
    "/orders/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="List User Orders",
    description="Return all orders for the specified user id. Restricted to staff/superuser accounts.",
)
async def get_user_orders(user_id: int, user:UserResponse = Depends(get_current_user), db:Session = Depends(get_db)):
    return await fetch_user_orders(user_id , user, db)


# Get a orders specific user [only that User and Superuser can perform]
@order_router.get(
    "/user/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Order",
    description="Retrieve a specific order. Only the order owner or staff can access this endpoint.",
)
async def get_specific_user_order(order_id: int, user:UserResponse = Depends
(get_current_user), db:Session = Depends(get_db)):
    return await fetch_specific_user_orders(order_id , user, db)


@order_router.patch(
    "/orders/update/{order_id}",
    response_model=PatchOrderResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update Order",
    description="Partially update an order's mutable fields. Owner or staff only.",
)
async def update_order(order_id:int ,data:PatchOrder, user: UserResponse = Depends(get_current_user), db:Session = Depends(get_db)):
    return await patch_order(order_id, data,user,db)


@order_router.patch(
    "/orders/status/{order_id}",
    response_model=PatchOrderResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update Order Status",
    description="Update only the order status (pending → in-transit → delivered).",
)
async def update_order_status(order_id:int, data: OrderStatusUpdate, user:UserResponse = Depends(get_current_user), db:Session = Depends(get_db)):
    return await patch_order_status(order_id, data, user, db)

@order_router.delete(
    "/orders/delete/{order_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete Order",
    description="Delete an order. Requires appropriate permissions (owner or staff).",
)
async def delete_order(order_id: int, user:UserResponse = Depends(get_current_user), db:Session = Depends(get_db)):
    return await remove_order(order_id, user, db)
