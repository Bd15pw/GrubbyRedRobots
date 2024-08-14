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
  driver.get("https://apps.powerapps.com/play/e/default-facac3c4-e2a5-4257-af76-205c8a821ddb/a/b06b201d-c7aa-4fb9-8400-3e5999985fb2?tenantId=facac3c4-e2a5-4257-af76-205c8a821ddb&source=AppSharedV3&hint=19f6ca8d-0213-463d-85e3-73e9c06e5518")
  return driver




def main():
  driver = get_driver()
  #time.sleep(2)
 # driver.find_element(By.ID, "id_username").send_keys("automated")  
  #time.sleep(2)
  #driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
  print(driver.current_url)

print(main())
