from fastapi import FastAPI
import logging
from pydantic import BaseModel
#import uvicorn

app = FastAPI()
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

'''class UserInput(BaseModel):
    name: str
    email: str
    password: str'''

users_list = [
    User(id=1, name='abc', email='abc@mail.com', password='123123')
]

@app.get('/users/')
async def users():
    logger.info('Отработал GET запрос')
    return

@app.get('/users/{id}')
async def user_by_id(id: int):
    for user in users_list:
        if user.id == id:
            return user
    logger.info('Отработал GET запрос')
    return {'message': 'Пользователь не найден'}

@app.post('/user_add/')
async def user_add(user: User):
    new_user = User(
        id=len(users_list) + 1,
        name=user.name,
        email=user.email,
        password=user.password
    )
    users_list.append(new_user)
    logger.info('Отработал POST запрос')
    return users_list

@app.put('/user_update/{user_id}')
async def user_update(user_id: int, user: User):
    for existing_user in users_list:
        if existing_user.id == user_id:
            existing_user.name = user.name
            existing_user.email = user.email
            existing_user.password = user.password
            logger.info(f'Отработал PUT запрос для пользователя с id = {user_id}')
            return existing_user
    return {'message': 'Пользователь не найден'}

@app.delete('/user_delete/{id}')
async def user_delete(id: int):
    for user in users_list:
        if user.id == id:
            users_list.remove(user)
    logger.info(f'Отработал DELETE запрос для user id = {id}')
    return users_list

#if __name__ == '__main__':
   # uvicorn.run('dz:app', host='127.0.0.1', port=8000, reload=True)


