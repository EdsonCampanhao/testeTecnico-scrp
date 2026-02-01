from fastapi import FastAPI
from services.scraper_service import get_product_service
from db.db_generator import db_generator
from services import db_service

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello World"}

@app.get("/get-product/{id}")
def get_product(id):
    try:
        prod=db_service.get_product(id)
        return{"prod":prod}
    except ValueError:
        return{"Error":"Valor de id não encontrado"}
    

@app.post("/create-product/{name}")
def create_product(name):
    prod=db_service.create_product(name)
    return prod

@app.put("/update-product/{id}")
def update_product(id):
    try:
        prod=db_service.update_product(id)
        return{"prod":prod}
    except ValueError:
        return{"Error":"Valor de id não encontrado"}
    
@app.delete("/delete-product/{id}")
def delete_product(id):
    try:
        return db_service.delete_product(id)
    except ValueError:
        return{"Error":"Valor de id não encontrado"}

    
    




