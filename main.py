from fastapi import FastAPI
from scraper import ProductScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello World"}


@app.get("/get-product/{name}")
def get_product(name):
    
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
#   options.add_argument("--headless")  # opcional
    options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
)
    driver = webdriver.Chrome(options=options)
    scraper = ProductScraper(driver)
    
    return{"user":scraper.search_product(name)}




