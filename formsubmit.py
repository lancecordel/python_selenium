ECHO is on.
#https://demoqa.com/automation-practice-form

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

website = "https://demoqa.com/automation-practice-form"
path = "/users/lwiltshire/downloads/chromedriver/"

#headless-mode
# options = Options()
# options.headless = True


service = Service(executable_path=path)
#driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()

driver.implicitly_wait(10)

firstName = driver.find_element(By.ID, "firstName")
driver.find_element(By.ID, "firstName").send_keys("Jerry")

driver.find_element(By.ID, "lastName").send_keys("Seinfeld")
print('lastName Passed')

driver.find_element(By.ID, "userEmail").send_keys("JerryS@funnyMan.com")
print('email Passed')

driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
male = driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
driver.execute_script("arguments[0].click()", male)
#ActionChains(driver).move_to_element(male).click().perform()
print('gender Passed')

#phoneNumber = driver.find_element(By.ID, "userNumber")
#driver.execute_script("arguments[0].scrollIntoView()", phoneNumber)
driver.find_element(By.ID, "userNumber").send_keys("5552226666")
print('number Passed')

#select date of birth drop down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']").click()

monthSelect = driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
yearSelect = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
ActionChains(driver).move_to_element(monthSelect).click().perform()

month = driver.find_element(By.XPATH, "//option[text()='May']")
day = driver.find_element(By.XPATH, "//div[text()='1']")

driver.find_element(By.XPATH, "//option[text()='May']").click()

#click month field again to verify choice
ActionChains(driver).move_to_element(monthSelect).click().perform()

#click year field
ActionChains(driver).move_to_element(yearSelect).click().perform()

#select a year
driver.find_element(By.XPATH, "//option[text()='1962']").click()

#click year field again to confirm
ActionChains(driver).move_to_element(yearSelect).click().perform()

#now select day
driver.find_element(By.XPATH, "//div[text()='1']").click()
print('Date Of Birth Passed')

# subjectInputField = driver.find_element(By.ID,  "subjectsInput")
# ActionChains(driver).move_to_element(subjectInputField).click().perform()
#ActionChains(driver).move_to_element(subjectInputField).click().perform()
driver.find_element(By.ID, "subjectsInput").send_keys("maths")
ActionChains(driver).key_down(Keys.ENTER).perform()
print('Subject Passed')

reading = driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-2']")
driver.execute_script("arguments[0].click();", reading)
print('Hobbies Passed')

driver.find_element(By.ID, "currentAddress").send_keys("This is my current address")
print('Address Passed')

#state  
ActionChains(driver).key_down(Keys.TAB).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

#city
ActionChains(driver).key_down(Keys.TAB).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

#submit
ActionChains(driver).key_down(Keys.TAB).key_down(Keys.ENTER).perform()


#iterate through descendents

# if stat:
#     print('found it!')
# else:
#     print('keep going')
#driver.find_element(By.XPATH, "//div[text()='Select State']").click()
#stateSelect = driver.find_element(By.XPATH, "//div[text()='Uttar Pradesh']")

#
# driver.find_element(By.XPATH, "//div[text()='Select City']").click()
# citySelect = driver.find_element(By.XPATH, "//div[text()='Agra']")
# ActionChains(driver).move_to_element(citySelect).click().perform()
#
# #Click submit
# driver.find_element(By.XPATH, "//button[@id='submit']").click()

#this also keeps browser running
while True:
    pass
