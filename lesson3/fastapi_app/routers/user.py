from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from lesson3.fastapi_app import schemas
from lesson3.fastapi_app.crud import create_user, get_users
from lesson3.fastapi_app import database

router = APIRouter(
    prefix="/users",
    tags=["user"]
)

get_db = database.get_db


@router.get("/")
async def users(db: Session = Depends(get_db)):
    return get_users(db)


@router.post("/create")
def user_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)