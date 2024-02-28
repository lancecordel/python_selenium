import os
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

website = "https://the-internet.herokuapp.com/javascript_alerts"
authenticationPopup = "https://the-internet.herokuapp.com/basic_auth"
iFramesTest = "https://selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
innerFrameTest = "https://demo.automationtesting.in/Frames.html"
browserWindowID = "https://opensource-demo.orangehrmlive.com/"

path = "/users/lwiltshire/downloads/chromedriver/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
#driver.get(website)
#driver.get(authenticationPopup)
#driver.get(iFramesTest)
#driver.get(innerFrameTest)
driver.get(browserWindowID)
driver.maximize_window()

#click button
#driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

#time.sleep(2)

#switch to alert windoq
#alertWindow = driver.switch_to.alert
#alertWindow.send_keys("Elow Govna")
#alertWindow.accept()
#alertWindow.dismiss()

#shortcut
#driver.switch_to.alert.accept()

#authentication popup
#ass soon as application is launched, user name and password is requested
#find elements will not work
#this will bypass alert window and go right to the home page
#driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
#------------------------------------------------------------------------------------------

#how to handle iframes
#find link by text
#frame, iframe and form are all types of frames
# driver.switch_to.frame("classFrame")
# firstFrameElement = driver.find_element(By.XPATH, "//a[text()='org.openqa.selenium']")
# driver.execute_script("arguments[0].click();", firstFrameElement)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("packageFrame")
# #putting click into javascript execution solved the blocked element exception in this case
# secondFrameElement = driver.find_element(By.LINK_TEXT, "WebDriver")
# driver.execute_script("arguments[0].click();", secondFrameElement)
# driver.switch_to.default_content()
#-------------------------------------------------------------------------------

#how to handle innerFrames
# driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
# outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
# driver.switch_to.frame(outerframe)
#
# innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
# driver.switch_to.frame(innerframe)
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")

#switch between browser windows
# windowID = driver.current_window_handle
# (print(windowID))
#------------------------------------------------------------------------
time.sleep(2)
link = driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIds = driver.window_handles

#appraoch 1, Looping is better
# parentWindowId = windowIds[0]
# childWindowId = windowIds[1]
# driver.switch_to.window(childWindowId)
# print(driver.title)

# driver.switch_to.window(parentWindowId)
# print(driver.title)

# #for loop approach
# for windowId in windowIds:
#     driver.switch_to.window(windowId)
#     print(driver.title)

# to close a specific browser window
for windowId in windowIds:
    driver.switch_to.window(windowId)
    if driver.title == "OrangeHRM":
        driver.close()
        #print(driver.title)






while True:
    pass