from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt 

def get_driver():
  #Set options 
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-featgures=AutomationControlled")


  driver=webdriver.Chrome(options)
  driver.get("https://titan22.com/account/login")
  return driver





def main():
  driver = get_driver()
  
  time.sleep(2)
  driver.find_element(By.ID, "CustomerEmail").send_keys("Bart.dziedzic15@gmail.com") 
  time.sleep(2)
  driver.find_element(By.ID, "CustomerPassword").send_keys("Bartek15pw"+ Keys.RETURN) 
  driver.find_element(By.XPATH, "/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
  time.sleep(2)
  print(driver.current_url)
 
 
  
  
  

print(main())
