from pydantic import BaseModel

class ProjectSchema(BaseModel):
    project_name: str
    district: str
    version: str

    class Config:
        orm_mode = True


class ProjectDB(ProjectSchema):
    id: int

    class Config:
        orm_mode = True


class AnkerWoWiSchema(BaseModel):
    kne: str
    coverage: float