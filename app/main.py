from fastapi import FastAPI

app = FastAPI(title="mini-slashdb")


@app.get("/")
def root():
    return {"message": "Welcome to mini-slashdb"}
