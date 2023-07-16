from fastapi import FastAPI
from src.routes.resources import router as ResourcesRouter

app = FastAPI()
app.include_router(ResourcesRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}
