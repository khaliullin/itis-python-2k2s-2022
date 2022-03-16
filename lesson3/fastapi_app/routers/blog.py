from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from lesson3.fastapi_app import database
from lesson3.fastapi_app import schemas, models

router = APIRouter(
    prefix="/blogs",
    tags=["blog"]
)

get_db = database.get_db



@router.post("/new")
async def new_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    db_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


@router.get("/")
async def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

