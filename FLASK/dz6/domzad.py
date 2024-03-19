from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import ForeignKey, Table, Column, Integer, String, create_engine, MetaData
import databases
from random import randint

DATABASE_URL = 'sqlite:///dbdz.db'

database = databases.Database(DATABASE_URL)
metadata = MetaData()

items = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('Item', String),
    Column('Description', String),
    Column('Price', String)
)

orders = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('User_id', Integer, ForeignKey('users.id')),
    Column('Item_id', Integer, ForeignKey('items.id')),
    Column('Order_day', String),
    Column('Order_status', String(50))
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('Name', String(30)),
    Column('Surname', String(30)),
    Column('Email', String(50)),
    Column('Password', String(50))
)

engine = create_engine(
    DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)

app = FastAPI()

class ItemIn(BaseModel):
    item: str = Field(..., max_length=30)
    description: str
    price: float = Field(..., le=100000, ge=0)

class Item(BaseModel):
    id: int
    item: str = Field(..., max_length=30)
    description: str
    price: float = Field(..., le=100000, ge=0)

class OrderIn(BaseModel):
    user_id: int
    item_id: int
    order_day: str = Field(...)
    order_status: str = Field(..., max_length=50)

class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    order_day: str = Field(...)
    order_status: str = Field(..., max_length=50)

class UserIn(BaseModel):
    name: str = Field(..., max_length=30)
    surname: str = Field(..., max_length=30)
    email: str = Field(..., max_length=50)
    password: str = Field(..., max_length=50)

class User(BaseModel):
    id: int
    name: str = Field(..., max_length=30)
    surname: str = Field(..., max_length=30)
    email: str = Field(..., max_length=50)
    password: str = Field(..., max_length=50)


#  ITEMS
    
@app.get('/fake_items/{count}')
async def create_note_item(count: int):
    for i in range(count):
        query = items.insert().values(Item = f'item{i}', Description = f'some_text', 
                                  Price = randint(1, 99999))
                                    
        await database.execute(query)
    return {'message': f'{count} fake items created'}


@app.post('/items/')
async def create_item(item: ItemIn):
    query = items.insert().values(item = item.item, description = item.description, 
                                  price = item.price)
    query = items.insert().values(**item.model_dump)
    last_record_id = await database.execute(query)
    return {**item.model_dump(), 'id': last_record_id}

@app.get('/items/')
async def read_items():
    query = items.select()
    return await database.fetch_all(query)

@app.get('/items/{id}')
async def read_item(id: int):
    query = items.select().where(items.c.id == id)
    return await database.fetch_one(query)

@app.put('/items/{id}')
async def update_item(id: int, new_item: ItemIn):
    query = items.select().where(items.c.id == id).values(**new_item.model_dump())
    await database.execute(query)
    return {**new_item.model_dump(), 'id': id}

@app.delete('/items/{id}')
async def delete_item(id: int):
    query = items.delete().where(items.c.id == id)
    await database.execute(query)
    return {'message': 'Item deleted'}


#  ORDERS

@app.get('/fake_orders/{count}')
async def create_note_order(count: int):
    for i in range(count):
        query = orders.insert().values(User_id = randint(1,20), Item_id = randint(1,20), 
                                  Order_day = f'{randint(1,28)}.{randint(1,12)}.2024',
                                    Order_status = f'some_txt')
        await database.execute(query)
    return {'message': f'{count} fake orders created'}

@app.post('/orders/')
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id = order.user_id, item_id = order.item_id, 
                                  order_day = order.order_day,
                                    order_status = order.order_status)
    query = orders.insert().values(**order.model_dump)
    last_record_id = await database.execute(query)
    return {**order.model_dump(), 'id': last_record_id}

@app.get('/orders/')
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)

@app.get('/orders/{id}')
async def read_order(id: int):
    query = orders.select().where(orders.c.id == id)
    return await database.fetch_one(query)

@app.put('/orders/{id}')
async def update_order(id: int, new_order: OrderIn):
    query = orders.select().where(orders.c.id == id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), 'id': id}

@app.delete('/orders/{id}')
async def delete_order(id: int):
    query = orders.delete().where(orders.c.id == id)
    await database.execute(query)
    return {'message': 'Order deleted'}


#  USERS

@app.get('/fake_users/{count}')
async def create_note_user(count: int):
    for i in range(count):
        query = users.insert().values(Name=f'user{i}', Surname=f'example{i}',
                                       Email=f'mail{i}@mail.ru', Password=f'123{i}')
        await database.execute(query)
    return {'message': f'{count} fake users created'}

@app.post('/users/')
async def create_user(user: UserIn):
    query = users.insert().values(name = user.name, surname = user.surname, 
                                  email = user.email,
                                    password = user.password)
    query = users.insert().values(**user.model_dump)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), 'id': last_record_id}

@app.get('/users/')
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@app.get('/users/{id}')
async def read_user(id: int):
    query = users.select().where(users.c.id == id)
    return await database.fetch_one(query)

@app.put('/users/{id}')
async def update_user(id: int, new_user: UserIn):
    query = users.select().where(users.c.id == id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), 'id': id}

@app.delete('/users/{id}')
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    await database.execute(query)
    return {'message': 'User deleted'}