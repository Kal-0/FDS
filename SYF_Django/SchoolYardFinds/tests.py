from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

class T0hostTest(LiveServerTestCase):
    def testHomePage(self):
        
        
        driver.get("http://127.0.0.1:8000/")
        #driver.get(self.live_server_url)
        
        
        time.sleep(0.5)
        assert "Schoolyard Finds" in driver.title
 
 
        
class T1registerFormTest(LiveServerTestCase):
    def testForm(self):
        wait = WebDriverWait(driver, 10)
        
        driver.get("http://127.0.0.1:8000/")
        #driver.get(self.live_server_url,"/accounts/login/")

        time.sleep(1)
        
        register_btn = driver.find_element(By.ID, "register1")
        
        register_btn.send_keys(Keys.RETURN)
        #pagina de cadastro
        assert "signup/" in driver.current_url
        
        time.sleep(1)
        
        
        username = driver.find_element(By.NAME, "username")
        email = driver.find_element(By.NAME, "email")
        password1 = driver.find_element(By.NAME, "password1")
        password2 = driver.find_element(By.NAME, "password2")
        register_btn = driver.find_element(By.ID, "submit_register1")
        
        username.send_keys("cadastroJaExistente")
        email.send_keys("cadastroJaExistente@gmail.com")
        password1.send_keys("senha1234")
        password2.send_keys("senha1234")
        time.sleep(3)
        
        register_btn.send_keys(Keys.RETURN)
        
        
        
        username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        password1 = wait.until(EC.element_to_be_clickable((By.NAME, "password1")))
        password2 = wait.until(EC.element_to_be_clickable((By.NAME, "password2")))
        register_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit_register1")))
        
        #clear fields
        username.clear()
        email.clear()
        password1.clear()
        password2.clear()
        
        username.send_keys("novoCadastro")
        email.send_keys("novoCadastro@gmail.com")
        password1.send_keys("senha1234")
        password2.send_keys("senha1234")
        time.sleep(2)
        
        register_btn.send_keys(Keys.RETURN)
        
        
        
        time.sleep(3)        
   
   
        
class T2loginFormTest(LiveServerTestCase):
    def testForm(self):
        wait = WebDriverWait(driver, 10)
        
        driver.get("http://127.0.0.1:8000/")
        #driver.get(self.live_server_url,"/accounts/login/")
        
        time.sleep(1)
        
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit_btn = driver.find_element(By.ID, "login1")
        
        
        username.send_keys("testeInexistente")
        password.send_keys("senha1234")
        time.sleep(2)
        submit_btn.send_keys(Keys.RETURN)
        time.sleep(2)
        
        
        #username = driver.find_element(By.NAME, "username")
        #password = driver.find_element(By.NAME, "password")
        #submit_btn = driver.find_element(By.ID, "login1")
        
        username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "login1")))
        
        
        username.clear()
        password.clear()
        username.send_keys("novoCadastro")
        password.send_keys("senha1234")
        time.sleep(2)
        
        submit_btn.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "home/" in driver.current_url
        
        
        
class T3addPublicationTest(LiveServerTestCase):
    def testForm(self):
        driver = webdriver.Chrome(executable_path=driver_path)
        
        wait = WebDriverWait(driver, 10)
        
        driver.get("http://127.0.0.1:8000/")
        #driver.get(self.live_server_url,"/accounts/login/")
        
        time.sleep(1)
        
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit_btn = driver.find_element(By.ID, "login1")
        
        
        username.send_keys("testeInexistente")
        password.send_keys("senha1234")
        time.sleep(2)
        submit_btn.send_keys(Keys.RETURN)
        time.sleep(2)
        
        
        #username = driver.find_element(By.NAME, "username")
        #password = driver.find_element(By.NAME, "password")
        #submit_btn = driver.find_element(By.ID, "login1")
        
        username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "login1")))
        
        
        username.clear()
        password.clear()
        username.send_keys("novoCadastro")
        password.send_keys("senha1234")
        time.sleep(2)
        
        submit_btn.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "home/" in driver.current_url
        
        

        
        