from fastapi import FastAPI

from api_project.adapters.api.tariffs.router import whatcrm_router

app = FastAPI()

app.include_router(whatcrm_router)


@app.get("/")
def test_end():
    return {"message": "Hello World"}
