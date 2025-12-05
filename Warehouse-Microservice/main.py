from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
class Product(HashModel):
    name: str
    price : float
    quantity: int
    class Meta:
        database = redis

@app.post('/product')
def create(product: Product):
    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )
    return new_product.save()


@app.get('/product/{pk}')
def get_product(pk: str):
    return Product.get(pk)

@app.get('/products')
def get_all_products():
    return [format(pk) for pk in Product.all_pks()]

def format(pk:str):
    product = Product.get(pk)
    return {
        'id' : product.pk,
        'name': product.name,
        'price' : product.price,
        'quantity': product.quantity
    }

@app.delete('/product/{pk}')
def delete(pk:str):
    return Product.delete(pk)

