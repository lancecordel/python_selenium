import time

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

#disable notifications
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
#---------------------------------------------------------
disableNotificationsTest = "https://whatmylocation.com"
webTablesTest = "https://testautomationpractice.blogspot.com"
webTableDynamicTest = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
path = "/users/lwiltshire/downloads/chromedriver/"


service = Service(executable_path=path)
#disable notification.  add options as an argument
driver = webdriver.Chrome(service=service, options=options)
driver.get(webTableDynamicTest)
driver.maximize_window()

#below is for webTablesTest = "https://testautomationpractice.blogspot.com"
#Traversing web tables
#count rows and columns of table

# #get all ancestors of element that are a row
# numberOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
# numberOfColumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
# # print(numberOfRows, numberOfColumns)
# #-----------------------------------------------------------------------------------------------------
#
# #read specific row and column data
# # tableData = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
# # print(tableData)
# #--------------------------------------------------------------------------
#
# #read all the rows and columns
# print('all the rows and columns of data')
# for row in range(2, numberOfRows + 1):
#     for column in range(1, numberOfColumns + 1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(column)+"]").text
#         #gives spacing at end of each line to make it look more like a table.
#         print(data, end = '      ')
#     print()
# #-------------------------------------------------------------
#
# #read data base on a condition
# for row in range(2, numberOfRows + 1):
#     authorName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[2]").text
#     if authorName == "Mukesh":
#         bookName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[1]").text
#         authorName = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[2]").text
#         price = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{row}]/td[4]").text
#         print(f"author: {authorName}            Book:{bookName}          price: {price}")
# print("----------------------------------------------------------------------------------------------")

#below is for webTableDynamicTest = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
#reading dynamic data from tables.
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
login = driver.find_element(By.XPATH, "//button[text()=' Login ']")
driver.execute_script("arguments[0].click();", login)

#wait a couple seconds before next execution
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//span[text()='User Management ']").click()

table = driver.find_elements(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div")

for row in table:
    columns = row.find_elements(By.XPATH, "./div/div")
    if columns[1].text == "Admin":
        edit = columns[5].find_element(By.XPATH, ".//button[2]")
        edit.click()
        break

statusDropDown = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div")
ActionChains(driver).move_to_element(statusDropDown).click().key_down(Keys.DOWN).key_down(Keys.DOWN).click().perform()

saveButton = driver.find_element(By.XPATH, "//button[text()=' Save ']")
driver.execute_script("arguments[0].click();", saveButton)

ActionChains(driver).move_to_element(saveButton).click().perform()
ActionChains(driver).move_to_element(saveButton).click().perform()

while True:
    pass


