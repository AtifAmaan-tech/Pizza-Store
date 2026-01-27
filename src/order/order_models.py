from src.utils.db import Base
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String,Integer, ForeignKey

class OrderModel(Base):
    __tablename__ = "order"

    ORDER_STATUS = (
        ('PENDING','pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED','delivered')
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large')
    )

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer,nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), default = 'pending')
    pizza_size = Column(ChoiceType(choices = PIZZA_SIZES), default = 'small')
    user_id = Column(Integer, ForeignKey("user.id") )
    user = relationship("UserModel", back_populates='order')

    def __repr__(self):
        return f"<Order: {self.id}>"