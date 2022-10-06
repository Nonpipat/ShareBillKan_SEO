from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.netflix.com/th/login')
email = driver.find_element(By.id('id_userLoginId'))
