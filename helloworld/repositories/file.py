from helloworld.models.file import File, FileCreate

from .base import BaseRepository


class FileRepository(BaseRepository[File, FileCreate]):
    table = File
