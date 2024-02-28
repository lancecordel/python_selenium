# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# website = "https://www.the-sun.com/"
# path = "/users/lwiltshire/downloads/chromedriver"
#
# service = Service(executable_path=path)
# driver = webdriver.Chrome(service=service)
#
# driver.get(website)



from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

website = "https://www.facebook.com/"
path = "/users/lwiltshire/downloads/chromedriver/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

#driver = webdriver.Chrome("/users/lwiltshire/downloads/chromedriver")
#driver.get("https://www.facebook.com/")

driver.get(website)
#driver.find_element(By.XPATH, "//input[@name='email']").send_keys("ads@gmail.com")
#driver.find_element(By.NAME, "email").clear()
#driver.find_element(By.ID, "pass").send_keys("12345678")
#driver.find_element(By.XPATH, "//button[@name='login']").click()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#Keeps selenium running
# while 1==1:
#     pass

#this also keeps browser running
# while True:
#     pass


# # sum of 1 - 100
# a = 12
# b = 0
# try:
#     c = a / b
#     print(c)
# except Exception as e:
#     print(str(e))
#     print("There is a error")

#below is for the demoqa.com page
driver.find_element(By.XPATH, '//span[')
