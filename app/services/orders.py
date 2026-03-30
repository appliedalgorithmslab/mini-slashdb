from typing import Optional

from sqlalchemy.orm import Session

from app import models, schemas


def create_order(db: Session, order: schemas.OrderCreate):
    user = db.query(models.User).filter(models.User.id == order.user_id).first()
    if not user:
        raise ValueError("User not found")

    db_order = models.Order(total=order.total, user_id=order.user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_orders(db: Session, user_id: Optional[int] = None, min_total: Optional[float] = None):
    query = db.query(models.Order)
    if user_id is not None:
        query = query.filter(models.Order.user_id == user_id)
    if min_total is not None:
        query = query.filter(models.Order.total >= min_total)
    return query.all()
