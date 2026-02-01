from time import sleep
from selenium.webdriver.common.by import By
from entities.product import Product
from urllib.parse import quote
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
        sleep(random.uniform(3, 5))
        
        #utilizando execute script para remover o modal dos cookies sem id.
        self.driver.execute_script("""
            var modal = document.querySelector('.modal-cookies');
            if(modal) modal.remove();
            """)        
        link = self.safe_call(self.get_link,'erro ao localizar link')
        nameProd = self.safe_call(self.get_name,"erro ao localizar nome") 
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
        name_tag = self.driver.find_element(By.XPATH,'//h3[@itemprop="name"][1]')
        name = name_tag.get_attribute("textContent")
        return name
        
    def get_link(self):
        link_tag=self.driver.find_element(By.XPATH,"//a[@class='w-app-link'][1]")
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