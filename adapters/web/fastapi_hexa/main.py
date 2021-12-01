from fastapi import FastAPI

from .router.api_v1.api_router import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def main_endpoint_test():
    return {"message": "Hello World"}
