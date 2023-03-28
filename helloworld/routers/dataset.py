from fastapi import (
    APIRouter,
    status,
    UploadFile,
    File,
    Depends,
)

from helloworld.schemas.dataset import UploadResponse
from helloworld.services.dataset import DatasetService
from helloworld.dependencies.service import get_dataset_service

router = APIRouter(tags=['dataset'])


@router.post(
    '/upload/',
    name='file:upload',
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    summary='Upload file to dataset',
)
async def upload(
        content: UploadFile = File(...),
        dataset_service: DatasetService = Depends(
            get_dataset_service
        ),
) -> UploadResponse:
    content_as_bytes = await content.read()
    id_, hash_content = await dataset_service.upload_file(
        filename=content.filename,
        content=content_as_bytes,
    )
    return UploadResponse(
        filename=content.filename,
        hash=hash_content,
        id=id_,
    )
