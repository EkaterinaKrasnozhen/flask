# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI, HTTPException
import logging
from fastapi.templating import Jinja2Templates
from typing import Optional
from pydantic import BaseModel
import uvicorn
#app = FastAPI(openapi_url="/api/v1/openapi.json")

app = FastAPI()

#pip install fastapi
#pip install "uvicorn[standard]"
#uvicorn ex_Fast_Api:app --reload
# посмотреть документацию /docs или /redoc (без тестирования)

    
class Task_in(BaseModel):
    title: str
    description: Optional[str]
    status: bool
    
class Task(Task_in):
    id: int
    
#tasks = [{'id':1, 'title': 'Задача #1', 'description': 'Информация о задаче #1', 'status': True}]
tasks = []


@app.get("/", response_model=list[Task])
async def read_tasks():
    return tasks


@app.post("/task/", response_model=Task)
async def create_task(item: Task_in): # post добавление новых данных
    id = len(tasks) + 1
    task = Task
    task.id = id
    task.status = item.status
    task.title = item.title
    task.description = item.description
    tasks.append(task)
    return task


@app.get("/{id}", response_model=Task)
async def get_task_by_id(id:int):
    for task in tasks:
        if task.id == id:
            return task


@app.put("/task_in/{id}", response_model=Task)# put для изменения данных сущетвующих что и на что
async def update_task(id: int, item: Task):
    for task in tasks:
        if task.id == id:
            task.status = item.status
            task.title = item.title
            task.description = item.description
            return task
    raise HTTPException(status_code=404, detail='Task not found')
    

@app.delete("/task/{id}")
async def delete_task(id: int):# лучше не удалять а isactive True/False
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return tasks
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    uvicorn.run(
    "Task1:app",
    host="127.0.0.1",
    port=8000,
    reload=True
    )