from fastapi import FastAPI
from routers import gateway

app = FastAPI()

app.include_router(gateway.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
