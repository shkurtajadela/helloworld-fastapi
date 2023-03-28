from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    id: int = Field(primary_key=True)

    created_at: Optional[datetime] = Field(
        sa_column_kwargs={'server_default': func.now()}
    )
    updated_at: Optional[datetime] = Field(
        sa_column_kwargs={'server_default': func.now()}
    )
