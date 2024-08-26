from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  output= float(text.split(": ")[1])
  return output



def main():
  driver = get_driver()
  time.sleep(2)
  driver.find_element(By.ID, "id_username").send_keys("automated")  
  time.sleep(2)
  driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
  time.sleep(2)
  text= driver.find_element(By.XPATH,"/html/body/div[1]/h1[2]").text
  return clean_text(text)
  
  

print(main())
