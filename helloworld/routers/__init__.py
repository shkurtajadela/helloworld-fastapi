from fastapi import APIRouter

from . import health
from . import dataset


router = APIRouter()
router.include_router(health.router, prefix='/health')
router.include_router(dataset.router, prefix='/dataset')
