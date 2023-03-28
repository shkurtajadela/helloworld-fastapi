from fastapi import Depends

from helloworld.dependencies.database import get_repository
from helloworld.repositories.file import (
    FileRepository,
)
from helloworld.services.dataset import DatasetService


def get_dataset_service(
    file_repository: FileRepository = Depends(get_repository(FileRepository)),
) -> DatasetService:
    return DatasetService(
        file_repository=file_repository,
    )
