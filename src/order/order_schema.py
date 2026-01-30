from pydantic import BaseModel
from typing import Optional, Literal


class OrderSchema(BaseModel):
    id: Optional[int] = None
    quantity: int 
    order_status: Literal['pending', 'in-transit', 'delivered'] = None
    pizza_size: Literal['small', 'medium', 'large', 'extra-large'] = None
    user_id: int = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "quantity": 2,
                "order_status": "pending",
                "pizza_size": "large",
                "user_id": 3
            }
        }

class OrderResponse(BaseModel):
    id: int
    quantity: int
    order_status: Literal['pending', 'in-transit', 'delivered']
    pizza_size: Literal['small', 'medium', 'large', 'extra-large']

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "quantity": 2,
                "order_status": "pending",
                "pizza_size": "large"
            }
        }

class PatchOrder(BaseModel):
    id: Optional[int] = None
    quantity: Optional[int] = None
    pizza_size: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "order_size": "pending",
                "pizza_size": "large"
            }
        }

class PatchOrderResponse(BaseModel):
    id: int
    quantity: int
    pizza_size: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "order_size": "pending",
                "pizza_size": "large"
            }
        }
