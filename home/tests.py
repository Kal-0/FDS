from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Documentação selenium para Python: https://selenium-python.readthedocs.io/
# Exemplos: https://ordinarycoders.com/blog/article/testing-django-selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)


# Create your tests here.

class TestHome(LiveServerTestCase):
    def test_title(self):
        browser.get('http://127.0.0.1:8000/')