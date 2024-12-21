from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title="AI Calculator API",
    description="An AI-powered calculator API using Gemini",
    version="1.0.0",
    lifespan=lifespan
)

ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', '*').split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "AI Calculator API is running",
        "documentation": "/docs",
        "environment": ENV}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])


if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))