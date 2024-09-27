
from fastcrud import crud_router
from fastcrud import FastCRUD

# from app.api.v1.settings.model import Item
from app.api.v1.settings.schema import CreateItemSchema, UpdateItemSchema
from app.core.db.database import get_session


# item_crud = FastCRUD(Item)


# item_router = crud_router(
#     session=get_session,
#     model=Item,
#     create_schema=CreateItemSchema,
#     update_schema=UpdateItemSchema,
#     crud=item_crud,
#     path="/items",
#     tags=["Items"],
# )
