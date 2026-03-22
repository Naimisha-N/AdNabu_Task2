from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
wait=WebDriverWait(driver,10)
driver.maximize_window()
pw=(By.ID,"password")
enter=(By.XPATH,"//button[contains(text(),'Enter')]")
search=(By.XPATH,f"(//summary[@role='button'])[2]")
search_input=(By.XPATH,"//input[@name='q']")
enter_search=(By.XPATH,"(//button[starts-with(@class,'search')])[1]")
product=(By.ID,"CardLink--7801364742234")
add=(By.XPATH,"//button[@name='add']")
cancel=(By.XPATH,"//button[starts-with(@class,'drawer')]")
cart=(By.ID,"cart-icon-bubble")
driver.get("https://adnabu-store-assignment1.myshopify.com")
wait.until(EC.visibility_of_element_located(pw)).send_keys('AdNabuQA')
wait.until(EC.element_to_be_clickable(enter)).click()
wait.until(EC.element_to_be_clickable(search)).click()
wait.until(EC.visibility_of_element_located(search_input)).send_keys("The Collection Snowboard: Liquid")
wait.until(EC.element_to_be_clickable(enter_search)).click()
wait.until(EC.element_to_be_clickable(product)).click()
wait.until(EC.element_to_be_clickable(add)).click()
wait.until(EC.element_to_be_clickable(cancel)).click()
wait.until(EC.element_to_be_clickable(cart)).click()
total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1920, total_height)
driver.save_screenshot("output.png")
driver.quit()