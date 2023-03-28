import pathlib
import hashlib
import logging

from helloworld.settings import settings
from helloworld.models.file import File, FileCreate
from helloworld.repositories.file import FileRepository
from helloworld.repositories.errors import UniqueViolationError
from helloworld.services.errors import (
    InvalidMimetypeError,
)


logger = logging.getLogger(__name__)


class DatasetService:
    def __init__(
            self,
            file_repository: FileRepository,
    ):
        self.file_repository = file_repository
        pass

    async def check_filename(self, filename: str) -> None:
        ext = pathlib.Path(filename).suffix
        if ext not in settings.ALLOWED_EXTENSION:
            raise InvalidMimetypeError(
                detail=f'Invalid object filename extension: {ext} '
            )

    async def hash(self, content: bytes) -> str:
        md5 = hashlib.md5()
        md5.update(content)
        return md5.hexdigest()

    async def upload_file(
            self,
            filename: str,
            content: bytes,
    ) -> tuple[int, str]:
        await self.check_filename(filename)
        hash_content = await self.hash(content)
        try:
            async with self.file_repository.connection.begin() as transaction:
                file = await self.file_repository.create(
                    FileCreate(
                        filename=filename,
                        hash=hash_content,
                    )
                )
        except UniqueViolationError as ex:
            logger.error(f"UploadDuplicateError: filename={filename}, hash={hash_content}")

        return file.id, hash_content
