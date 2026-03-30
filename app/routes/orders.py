from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.services import orders as order_service

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        return order_service.create_order(db, order)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.get("", response_model=list[schemas.OrderResponse])
def get_orders(
    user_id: Optional[int] = None,
    min_total: Optional[float] = None,
    db: Session = Depends(get_db),
):
    return order_service.get_orders(db, user_id=user_id, min_total=min_total)


@router.get("/user/{user_id}", response_model=list[schemas.OrderResponse])
def get_orders_for_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()
