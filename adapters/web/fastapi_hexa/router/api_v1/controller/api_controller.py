from fastapi import APIRouter

router_controller = APIRouter()


@router_controller.get("/")
async def api_test():
    return {"message": "test"}
