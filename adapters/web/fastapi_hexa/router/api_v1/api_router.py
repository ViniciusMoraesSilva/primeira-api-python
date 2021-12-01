from fastapi import APIRouter

from .controller.api_controller import router_controller

router = APIRouter()

router.include_router(router_controller, prefix="/test", tags=["test"])
