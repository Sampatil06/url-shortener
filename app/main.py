from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import auth
import app.models  # noqa: F401

app = FastAPI(
    title="URL Shortener",
    description="URL Shortener with Analytics API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)


@app.get("/health")
async def health_check():
    return {"status": "ok", "app": settings.BASE_URL}