from typing import Union
from fastapi import FastAPI
import os
from db.mongo import Database
from routes import generate
from src.routes import search

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    Database.init(mongo_uri)
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
async def shutdown_db_client():
    Database.close_client()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(generate.router)
app.include_router(search.router)