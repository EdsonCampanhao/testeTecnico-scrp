from scraper.scraper import ProductScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_product_service(name:list|str):
    
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    driver = webdriver.Chrome(options=options)
    scraper = ProductScraper(driver)
    
    if type(name) == list:
        prods = []
        for i in name:
            prods.append(scraper.search_product(i))
        driver.quit()
        return prods
    else:
        prod=scraper.search_product(name)
        driver.quit()
        return prod
    