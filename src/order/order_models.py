from src.utils.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String, ForeignKey

class OrderModel(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer,nullable=False)
    order_status = Column(String(50), default='pending')
    pizza_size = Column(String(50), default='small')
    user_id = Column(Integer, ForeignKey("user.id") )
    user = relationship("UserModel", back_populates='order')

    def __repr__(self):
        return f"<Order: {self.id}>"