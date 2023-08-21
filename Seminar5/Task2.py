# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI, HTTPException
import logging
from fastapi.templating import Jinja2Templates
from typing import Optional
from pydantic import BaseModel
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="templates")

app = FastAPI()

class Genre(BaseModel):
    id: int
    name: str
    
class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: Genre
    
movies = [
    Movie(id=1, title='Рио', description='детский контент', genre=Genre(id=1, name='mult')),
    Movie(id=2, title='Трансформеры', description='взрослый контент', genre=Genre(id=2, name='thriller')),
    Movie(id=3, title='Мачеха', description='семейный контент', genre=Genre(id=3, name='drama'))]

genres = [Genre(id=1, name='mult'), Genre(id=2, name='thriller'), Genre(id=3, name='drama')]


@app.get("/", response_model=list[Movie], summary='Получить список фильмов по жанру', tags=['Фильмы'])
async def get_movies(id:int):
    res_list = []
    for movie in movies:
        if movie.genre.id == id:
            res_list.append(movie)
    return res_list


if __name__ == '__main__':
    uvicorn.run(
    "Task2:app",
    # host="127.0.0.1",
    # port=8000,
    reload=True
    )