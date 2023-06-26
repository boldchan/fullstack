from typing import List
from fastapi import APIRouter, HTTPException

from src.database.models import ProjectSchema, ProjectDB
from src.api import crud


router = APIRouter()

@router.post("/", response_model=ProjectDB, status_code=201)
def create_project(project: ProjectSchema):
    project_id = crud.post_project(project)
    response_object = {
        "id": project_id,
        **project.dict()
    }
    print(response_object)
    return response_object


@router.get("/{id}/", response_model=ProjectDB)
def read_project(id: int):
    project = crud.get_project(id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/", response_model=List[ProjectDB])
def read_all_projects():
    return crud.get_all_projects()