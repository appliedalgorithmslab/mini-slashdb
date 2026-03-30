from typing import List, Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    total: float
    user_id: int


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    orders: Optional[List[OrderResponse]] = []

    class Config:
        from_attributes = True
