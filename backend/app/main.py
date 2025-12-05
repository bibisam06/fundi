# backend/app/main.py

from fastapi import FastAPI
from api import funding
app = FastAPI()
app.include_router(funding.router)
# app.include_router(items.router)
# app.include_router(users.router)
# app.include_router(admins.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

