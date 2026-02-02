from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.app.api.v1.api import api_router
from backend.app.core.config import settings

app = FastAPI(
    title="Guwahati Heritage Experiences API",
    description="Micro-itinerary booking platform for Guwahati heritage tours",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Guwahati Heritage Experiences API",
        "version": "1.0.0",
        "docs": "/api/docs"
    }