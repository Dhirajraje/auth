from fastapi import FastAPI
from pydantic import BaseModel
from app.api import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Auth Service",
    description="Authentication and Authorization Service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    debug=True,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow cookies, authorization headers, etc.
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


app.include_router(api_router, prefix="/api")


# Define a response model for the ping endpoint
class StatusResponse(BaseModel):
    """Response model for the ping endpoint."""

    status: str


# Simple health check endpoint
@app.get("/ping", tags=["Health"], response_model=StatusResponse)
async def ping():
    """Health check endpoint that returns a simple "pong!" message."""
    return {"status": "Alive :)"}
