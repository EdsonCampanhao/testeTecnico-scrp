from openpyxl import Workbook
from entities.product import Product
import openpyxl
from pathlib import Path
from services.scraper_service import get_product_service

# grab the active worksheet
def db_generator():
    names=extract_names("worten.xlsx")
    scraped_prods = get_product_service(names)
    create_new_db(scraped_prods)
    
    
def extract_names(path):
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    names:list[str]=[]
    
    for row in ws.iter_rows(min_row=2, values_only=True): 
        if None in row: 
            continue
        name=row[2]
        names.append(name)
    
    return names

def create_new_db(data):
    
    base_dir = Path(__file__).resolve().parent  # pasta db/
    db_path = base_dir / "db.xlsx"
    
    
    wb = Workbook()
    ws = wb.active
    create_header(ws)
    for i, prod in enumerate(data, start=2):  # Começar a partir da linha 2
        create_line(ws, i, prod)
    
    wb.save(db_path)
    wb.close()

    
def create_header(ws):
        ws['A1'] = "ID"
        ws['B1'] = "Nome"
        ws['C1'] = "Preço_mais_baixo"
        ws['D1'] = "Vendedor"
        ws['E1'] = "Link"
        

def create_line(ws,i,prod:Product):        
    # Preenche uma linha com os dados do item
    ws.cell(row=i, column=1, value=i-1)  # A coluna A é o ID, que será 'i-1'
    ws.cell(row=i, column=2, value=prod.name)  # Coluna B: Nome
    ws.cell(row=i, column=3, value=prod.lowestPrice)  # Coluna C: Preço
    ws.cell(row=i, column=4, value=prod.sellerName)  # Coluna D: Vendedor
    ws.cell(row=i, column=5, value=prod.link)  # Coluna D: Vendedor

    


