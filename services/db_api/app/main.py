import uvicorn
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="DB API Microservice",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"status": "API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
