from fastapi import APIRouter


from .user.router import user_router
from .auth.router import auth_router
from .settings.router import item_router as settings_router


router = APIRouter()

router.include_router(user_router,prefix='/user')
router.include_router(auth_router,prefix='/auth')
router.include_router(settings_router,prefix='/settings')