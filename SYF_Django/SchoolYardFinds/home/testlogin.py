from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Configura o driver do Selenium
driver = webdriver.Chrome(ChromeDriverManager().install())

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
