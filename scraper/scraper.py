from time import sleep
from selenium.webdriver.common.by import By
from entities.product import Product
from urllib.parse import quote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
        
products:list[Product] = []
    
    
    
class ProductScraper:
    def __init__(self,driver):
        self.driver=driver
        pass

    def search_product(self, name: str):
    
        if name is None or not isinstance(name, str):
            return None 
    
        name = quote(name)
        self.driver.get(f"https://www.worten.pt/search?query={name}&sort_by=rank-price&order_by=asc")
        
        nameProd = self.safe_call(self.get_name,"erro ao localizar nome")      
        link = self.safe_call(self.get_link,'erro ao localizar link')
        lowest_price = self.safe_call(self.get_lowest_price,"erro ao localizar valor")
        seller_name = self.safe_call(self.get_seller_name,"erro ao localizar nome")
        
        prod=Product(
            
            nameProd,
            link,
            lowest_price,
            seller_name,
        )
        
        return prod
      
    def get_name(self):
        name_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@itemprop="name"][1]'))
        )
        sleep(5)
         #utilizando execute script para remover o modal dos cookies sem id.
        self.driver.execute_script("""
            var modal = document.querySelector('.modal-cookies');
            if(modal) modal.remove();
            """)   
        
        name = name_tag.get_attribute("textContent")
        return name
        
    def get_link(self):
        link_tag=self.driver.find_element(By.XPATH,"//a[@itemprop='url'][1]")
        link=link_tag.get_attribute('href')
        return link
        
    def get_lowest_price(self):
        value_tag = self.driver.find_element(By.XPATH,'//span[@class="value"][1]')
        value=value_tag.get_attribute("textContent") 
        decimal_tag = self.driver.find_element(By.XPATH,'//sup[@class="decimal"][1]')
        decimal=decimal_tag.get_attribute("textContent")
        return float(f"{value}.{decimal}")
    
    def get_seller_name(self):
        seller_tag = self.driver.find_element(By.XPATH,'//b[@itemprop="seller"][1]')
        seller_name = seller_tag.get_attribute("textContent")
        return seller_name
    
    def safe_call(self,func,fallback_message):
        try:
            return func()
        except Exception as e:
            return f"{fallback_message}: {e}"