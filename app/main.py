from fastapi import FastAPI

from app.db import Base, engine
from app.routes import orders, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="mini-slashdb")

app.include_router(users.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "Welcome to mini-slashdb"}
