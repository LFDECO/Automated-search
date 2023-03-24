from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="C:\Program Files (x86)\chromedriver.exe"
n=int(input("enter 1 for anime and 2 for youtube"))
#for anime section
if n==1:
    srch=input("enter what to search")
    driver = webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    driver.get("https://zoro.to/")
    search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "keyword")))#telling driver to wait until the search box is clickable
    driver.execute_script("arguments[0].click();", search_input)#handling the exception if the element is getting overlapped by some other element and is not clickable we forcingg the click
    search_input.send_keys(srch)
    search_input.send_keys(Keys.ENTER)
elif n==2:
   srch1=input("enter")
   driver = webdriver.Chrome(executable_path=path)
   driver.maximize_window()
   driver.get("https://www.youtube.com/")
   search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]')))
   search_input.click()
   search_input.send_keys(srch1)
   search_input.send_keys(Keys.ENTER)
while True:
    pass

    
    