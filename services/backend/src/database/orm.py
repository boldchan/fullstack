import datetime
from typing import List, Optional
from sqlalchemy import ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "standard_planning_project"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    project_name: Mapped[str] = mapped_column(String(250))
    district: Mapped[str] = mapped_column(String(5))
    version: Mapped[str] = mapped_column(String(8))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    anker_wowis: Mapped[List["AnkerWoWi"]] = relationship(back_populates="project")

    def __repr__(self) -> str:
        return f"Project(id={self.id}, project_name={self.project_name}, district={self.district}, version={self.version}, created at {self.created_at}, last modified at {self.modified_at})"


class AnkerWoWi(Base):
    __tablename__ = "standard_planning_anker_wowi"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    kne: Mapped[str] = mapped_column(String(256))
    coverage: Mapped[float] = mapped_column(Float)
    project_id: Mapped[int] = mapped_column(ForeignKey("standard_planning_project.id")) 
    project: Mapped["Project"] = relationship(back_populates="anker_wowis")

    def __repr__(self) -> str:
        return f"AnkerWowi(id={self.id}, kne={self.kne}, coverage={self.coverage})"