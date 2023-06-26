from sqlalchemy.orm import Session
from sqlalchemy import select

from src.database.models import ProjectSchema
from src.database.orm import Project
from src.database.db import engine


def post_project(project: ProjectSchema):
    with Session(engine) as session:
        db_project = Project(**project.dict())
        session.add(db_project)
        session.commit()
        session.refresh(db_project)
        return db_project.id
    

def get_project(id: int):
    with Session(engine) as session:
        project_obj = session.get(Project, id)
        return project_obj
    

def get_all_projects():
    with Session(engine) as session:
        statement = select(Project)
        projects = session.scalars(statement).all()
        return projects