import openpyxl
from pathlib import Path
from services.scraper_service import get_product_service
from entities.product import Product
import openpyxl

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "db.xlsx"

def get_product(id):
    wb = openpyxl.load_workbook(DB_PATH)
    ws=wb.active()
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] == id:
            prod = Product(
                row[1],
                row[2],
                row[3],
                row[4]
            )
            # id está sendo posto aqui, pois o campo de atributo id só foi criado após a criação do db
            prod.id=row[0]
            wb.close()
            return prod
    return None

def create_product(name):
    wb = openpyxl.load_workbook(DB_PATH)
    ws=wb.active
    
    prod = get_product_service(name)
    prod.id=ws[f"A{ws.max_row}"].value+1
    
    ws.append([prod.id,prod.name,prod.lowestPrice,prod.sellerName,prod.link])
    wb.save(DB_PATH)
    
    return prod
    
    
       
    
    



