from sqlmodel import SQLModel, UniqueConstraint

from .base import BaseModel


class FileBase(SQLModel, table=False):
    filename: str
    hash: str
    size: int


class File(BaseModel, FileBase, table=True):
    __table_args__ = (UniqueConstraint('hash'),)


class FileCreate(FileBase):
    pass
