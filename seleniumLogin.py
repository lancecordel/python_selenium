from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

website = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
path = "/users/lwiltshire/downloads/chromedriver/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()


#Keeps selenium running
# while 1==1:
#     pass

#this also keeps browser running
while True:
    pass
