from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from more_itertools import quantify
from redis_om import get_redis_connection,HashModel
from settings import credentials

app = FastAPI(
    title="Store API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host= credentials.host,
    port= credentials.port, 
    password= credentials.password,
    decode_responses=True
)

class ProductOrder(HashModel):
    product_id : int
    quantity: int
    class Meta:
        database = redis

class Order(HashModel):
    product_id : str
    price : float
    fee : 
