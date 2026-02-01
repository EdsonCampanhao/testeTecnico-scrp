from fastapi import FastAPI
from services.scraper_service import get_product_service
from db.db_generator import db_generator

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello World"}

@app.get("/get-product/{name}")
def get_product(name):
    prod=get_product_service(name)
    return{"prod":prod}

    
    




