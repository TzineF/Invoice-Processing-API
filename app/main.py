from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
async def health():
    return {"status": "ok"}

app.include_router(router)