from fastapi import FastAPI

from src.api import ping, project
from src.database.db import engine, metadata


metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def hello_world():
    return {"hello": "world"}


app.include_router(ping.router)
app.include_router(project.router, prefix='/projects', tags=['projects'])