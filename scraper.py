from time import sleep
from selenium.webdriver.common.by import By


class Product:
    def __init__(self,name:str,link:str,lowestPrice:float,sellersName:str):
        self.name=name
        self.link=link
        self.lowestPrice=lowestPrice
        self.sellersName=sellersName
        

products:list[Product] = []
    
    
    
class ProductScraper:
    def __init__(self,driver):
        self.driver=driver
        pass

    def search_product(self, name: str):
        
        self.driver.get(f"https://www.worten.pt/search?query={name}&sort_by=rank-price&order_by=asc")
        sleep(7)
        
        #utilizando execute script para remover o modal dos cookies sem id.
        self.driver.execute_script("""
            var modal = document.querySelector('.modal-cookies');
            if(modal) modal.remove();
            """)        
        link = self.safe_call(self.get_link,'erro ao localizar link')
        self.driver.get(link)
        sleep(3)
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
        name_tag = self.driver.find_element(By.XPATH,'//h1[@class="product-header__title"]/span')
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
        seller_tag = self.driver.find_element(By.XPATH,'//div[@class="product-price-info__seller--inline product-price-info__seller"]/div/a/span')
        seller_name = seller_tag.get_attribute("textContent")
        return seller_name
    
    def safe_call(self,func,fallback_message):
        try:
            return func()
        except Exception as e:
            return f"{fallback_message}: {e}"