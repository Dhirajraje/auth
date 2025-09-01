from fastapi import FastAPI
from pydantic import BaseModel
from app.api import router as api_router


app = FastAPI(
    title="Auth Service",
    description="Authentication and Authorization Service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    debug=True,
)


app.include_router(api_router, prefix="/api")




# Define a response model for the ping endpoint
class StatusResponse(BaseModel):
    '''Response model for the ping endpoint.'''
    status: str

# Simple health check endpoint
@app.get("/ping", tags=["Health"],response_model=StatusResponse)
async def ping():
    '''Health check endpoint that returns a simple "pong!" message.'''
    return {"status": "Alive :)"}