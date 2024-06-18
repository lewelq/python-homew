from fastapi import FastAPI
import logging
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def fast():
    return {'msg': 'hello world'}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

@app.get('/root/')
async def read_root():
    logger.info('Отработал GET запрос')
    return {'hello': 'world'}

@app.post('/post/')
async def create(item: Item):
    logger.info('Отработал POST запрос')
    return item

