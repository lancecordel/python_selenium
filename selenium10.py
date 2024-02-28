import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#implement headless mode
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

datePickerTest = "https://jqueryui.com/datepicker/"
path = "/users/lwiltshire/downloads/chromedriver/"


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(datePickerTest)
driver.maximize_window()

#handling date pickers
#1. sending direct text date
#swtich to date frame
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("01/21/1990")

#2. traverse through element to pick individual date nodes
driver.switch_to.frame(0)

while True:
    driver.find_element(By.XPATH, "//")


year = "2020"
month = "january"
day = "14"

while True:
    pass