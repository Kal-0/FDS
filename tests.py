from django.test import LiveServerTestCase
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#windows:
driver_path = r"chromedriver.exe"

#linux-tests
driver_path = r"TestDrivers/chromedriver"



timeout = 10

service = Service()

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")




global driver


#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Chrome(executable_path=driver_path, options=options)


driver.set_page_load_timeout(timeout)

print("/////////////chromeDriver SET\n")


