from fastapi import APIRouter, Response
from database import *
from models import *
from typing import List

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru', password=f'{i}qweasd')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    """Create new user

    Args:
        user (UserIn): _model user without id_

    Returns:
        _type_: _dict_
    """
    query = users.insert().values(name=user.name, email=user.email)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@router.get("/users/", response_model=List[User])
async def read_users():
    """get all users

    Returns:
        _type_: _select all users from table_
    """
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user _id}" , response_model=User)
async def read_user(user_id: int):
    """returns one user by id

    Args:
        user_id (int): _input id_

    Returns:
        _type_: _select by user_id_
    """
    query = users.select(). where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
