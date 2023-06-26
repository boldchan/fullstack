from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
from tortoise import Tortoise  # NEW

from src.database.config import TORTOISE_ORM         # NEW
from src.database.register import register_tortoise  # NEW


# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")  # NEW

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
async def root():
    return {"message": "Hello World234"}

# @app.post("/add_project")
# async def addProject(proj: Project):
#     return proj
