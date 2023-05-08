from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Cria um objeto Service com o caminho do driver
service = Service(ChromeDriverManager().install())

# Configura o driver do Selenium com o objeto Service
driver = webdriver.Chrome(service=service)

# Acessa a página de login
driver.get('http://localhost:8000/login/')

# Encontra os campos de usuário e senha e preenche com os valores desejados
username_field = driver.find_element_by_css_selector('input[name="username"]')
password_field = driver.find_element_by_css_selector('input[name="password"]')
username_field.send_keys('admin')
password_field.send_keys('123')

# Encontra o botão de login e clica nele
login_button = driver.find_element_by_xpath('//button[@type="submit"]')
login_button.click()

# Fecha o navegador
driver.quit()
