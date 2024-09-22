from fastapi import FastAPI
from .api.api_router import router as api_router

from .core.db.database import engine, Base



async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Authentication service",redirect_slashes=True,lifespan=lifespan)


app.include_router(api_router,prefix='/api')



@app.get('/health',tags=['Health check'])
async def health():
    return {
        'status':'Okiee ^_^'
    }