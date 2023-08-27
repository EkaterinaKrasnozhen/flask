from fastapi import APIRouter
from database import *
from models import *

router = APIRouter()


@router.get("/fake_posts/")
async def create_post():
        query = posts.insert().values(user_id = 10, post=f'Hello my friend')
        await database.execute(query)
        return {'ok'}


@router.get("/posts/")
async def read_posts():
    query = sqlalchemy.select(
        posts.c.id, 
        users.c.id.label("user_id"),
        posts.c.post).join(users)
    return await database.fetch_all(query)
    
    
@router.post("/posts/", response_model=dict)
async def new_post(post: PostIn):
    query = posts.insert().values(user_id=post.user_id, post=post.post)
    last_record_id = await database.execute(query)
    return {**post.model_dump(), "id": last_record_id}