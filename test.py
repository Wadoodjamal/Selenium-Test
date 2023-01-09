from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options
# options = Options()
# options.headless = True

PATH = r"C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)
# driver = webdriver.Chrome(options=options)
# driver(options=options)

driver.get('http://localhost:3000/')
addButton = driver.find_element("xpath","/html/body/div[1]/form/button[1]")
addTaskInput = driver.find_element("xpath","/html/body/div[1]/form/input")
addTaskCheckbox = driver.find_element("xpath","/html/body/div[1]/form/li[1]/input")
removeTaskButton = driver.find_element("xpath","/html/body/div[1]/form/button[2]")
completeTaskCheckbox = driver.find_element("xpath","/html/body/div[1]/li[1]/input")

print('Test 1')
try:
    addTaskInput.send_keys('New task')
    addButton.click()
    time.sleep(3)
    print('Task Added')
    time.sleep(3)
except:
    print('Add Task Failed')

print('Test 2')
try:
    addTaskCheckbox.send_keys(True)
    if(addTaskCheckbox.is_selected()):
        removeTaskButton.click()
        print('Task Removed Successfully')
        time.sleep(3)
    else:
        print('Select Task First To Remove')
        time.sleep(3)
    print('Task Removed Test Case')
    time.sleep(3)
except:
    print('Remove Task Failed')

print('Test 3')
try:
    if(completeTaskCheckbox.is_selected()):
        completeTaskCheckbox.send_keys(False)
        print('Completed Task Removed')
        time.sleep(3)
    else:
        completeTaskCheckbox.send_keys(True)
        print('Completed Task Checked')
        time.sleep(3)
    print('Task Complete Test Case')
    time.sleep(3)
except:
    print('Complete Task Failed')