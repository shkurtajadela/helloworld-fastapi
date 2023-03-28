from pydantic import BaseModel, Extra


class UploadResponse(BaseModel):
    filename: str
    hash: str
    id: int

    class Config:
        extra = Extra.forbid
