from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.example.com")

element = driver.find_element(By.ID, "name")
