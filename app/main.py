from fastapi import FastAPI
from .api.api_router import router as api_router


app = FastAPI(title="Authentication service",redirect_slashes=True)


app.include_router(api_router,prefix='/api')



@app.get('/health',tags=['Health check'])
async def health():
    return {
        'status':'Okiee ^_^'
    }