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
import xlrd


# Creating new directory
def create_screenshot_directory():
    ss_dir = "./Screenshot"
    if not os.path.exists(ss_dir):
        os.makedirs(ss_dir)
    return ss_dir


# Capturing Screenshot
def take_ss(step_name, ss_dir):
    screenshot_name = step_name + ".png"
    driver.save_screenshot(ss_dir + "/" + screenshot_name)

create_screenshot_directory()

website = "https://itera-qa.azurewebsites.net/home/automation"
path = "/users/lwiltshire/downloads/chromedriver/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
driver.maximize_window()

# Creating New File:
try:
    wb = xlrd.open_workbook("data.xlsx")
    sheet1 = wb.sheet_by_index(0)
    cnt_row = sheet1.nrows
    cnt_rows = sheet1.nrows
    num_columns = sheet1.ncols
except Exception as e:
    print("Error reading excel file")

name = driver.find_element(By.ID, "name");
phone = driver.find_element(By.ID, "phone");
email = driver.find_element(By.ID, "email");
password = driver.find_element(By.ID, "password");
address = driver.find_element(By.ID, "address");
submit = driver.find_element(By.NAME, "submit");
genderSelect = driver.find_element(By.XPATH, "//label[text()='Gender']");
days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
dropLabel = driver.find_element(By.XPATH, "//div[text()='DropDown practice']")

driver.implicitly_wait(2)
for i in range(1, cnt_rows):
    namecell = sheet1.cell_value(i, 0)
    phonecell = sheet1.cell_value(i, 1)
    emailcell = sheet1.cell_value(i, 2)
    passwordcell = sheet1.cell_value(i, 3)
    addresscell = sheet1.cell_value(i, 4)
    gendercell = sheet1.cell_value(i, 5)
    daycell = sheet1.cell_value(i, 6)
    countrycell = sheet1.cell_value(i, 7)
    timecell = sheet1.cell_value(i, 8)
    methodcell = sheet1.cell_value(i, 9)

    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys(namecell)

    driver.find_element(By.ID, "phone").clear()
    driver.find_element(By.ID, "phone").send_keys(phonecell)

    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(emailcell)

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(passwordcell)

    driver.find_element(By.ID, "address").clear()
    driver.find_element(By.ID, "address").send_keys(addresscell)

    #scroll to gender view
    driver.execute_script("arguments[0].scrollIntoView()", genderSelect)
    driver.find_element(By.XPATH, f"//input[contains(@id, '{gendercell}')]").click()

    #clear days from previous user
    for day in days:
        if day.is_selected():
            day.click()

    #then make current selection
    driver.find_element(By.XPATH, f"//input[contains(@id, '{daycell}')]").click()

    #click dropdown
    driver.execute_script("arguments[0].scrollIntoView()", dropLabel)
    dropMenu = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div/select")

    #loop through option to select the one matching record matching speadsheet
    select = Select(driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div/select"))
    for country in select.options:
        if country.text == countrycell:
            country.click()
            #print(country.text)


    #years of experience
    experience = driver.find_element(By.XPATH, f"//label[contains(text(), '{timecell}')]")
    ActionChains(driver).move_to_element(experience).click().perform()

    #automation tools used
    # midway = driver.find_element(By.XPATH, "//label[contains(text(), 'enium')]")
    # driver.execute_script("arguments[0].scrollIntoView()", midway)
    # tools = driver.find_elements(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]//input")
    # for tool in tools:
    #     if tool.is_selected():
    #         tool.click()

    tool = driver.find_element(By.XPATH, f"//input[@id='{methodcell}']")
    ActionChains(driver).move_to_element(tool).click().perform()

    #take screen shot
    take_ss(namecell, "./Screenshot")


















#Keeps selenium running
# while 1==1:
#     pass

#this also keeps browser running
while True:
     pass
