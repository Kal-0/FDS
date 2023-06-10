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
#service = Service()
options = webdriver.ChromeOptions()
#options.add_argument("--no-sandbox")
#options.add_argument("--headless")
options.add_argument("--disable-gpu")



global driver


#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
 #driver = webdriver.Chrome(executable_path=driver_path, options=options)


driver.set_page_load_timeout(timeout)
print("/////////////chromeDriver SET\n")
global decoy_user, logged_in, decoy_publication
decoy_user = False
logged_in = False
decoy_publication = False



class T0hostTest(LiveServerTestCase):
    def testHomePage(self):
        
        
        driver.get("http://127.0.0.1:8000/")
        #driver.get(self.live_server_url)
        
        
        time.sleep(0.5)
        assert "Schoolyard Finds" in driver.title
 
  
     
class T1registerFormTest(LiveServerTestCase):
    def testForm(self):
        global decoy_user
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
        time.sleep(2)
        
        
        print("case 0000")
        
        #decoy already-exists-account doesnt exists case
        if "signup/" not in driver.current_url:
            register_btn = driver.find_element(By.ID, "register1")
            
            print("case 1111")
            
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
            
            
        
        time.sleep(3)
        
        
        
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
        
        print(driver.current_url)
        #assert "signup/" not in driver.current_url
        time.sleep(3)
        
        decoy_user = True 
   
   
        
class T2loginFormTest(LiveServerTestCase):
    def testForm(self):
        global decoy_user, logged_in
        wait = WebDriverWait(driver, 10)
        
        print(f"///////////////////decoy_user: {decoy_user}")
        if decoy_user == False:
            T1registerFormTest.testForm(self)
        
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
        
        
        logged_in = True
        
        
        
class T3addPublicationTest(LiveServerTestCase):
    def testForm(self):
        global logged_in, decoy_publication
        wait = WebDriverWait(driver, 10)

        if logged_in == False:
            T2loginFormTest.testForm(self)

        driver.get("http://127.0.0.1:8000/home/")

        time.sleep(2)

        for i in range(3):  # Adiciona 3 publicações
            addPub_btn = driver.find_element(By.NAME, "add_publication")
            addPub_btn.send_keys(Keys.RETURN)
            assert "publicacao/" in driver.current_url
            time.sleep(2)

            productName = driver.find_element(By.NAME, "productName")
            productCategory = driver.find_element(By.NAME, "productCategory")
            productPrice = driver.find_element(By.NAME, "productPrice")
            productDescription = driver.find_element(By.NAME, "productDescription")

            productName.send_keys(f"newProduct{i+1}")  # Nome diferente para cada publicação
            productCategory.send_keys("-newProductCategory")
            productPrice.send_keys("9.90")
            productDescription.send_keys("newProductDescription")
            time.sleep(4)

            publish_btn = driver.find_element(By.NAME, "publish_btn")
            publish_btn.send_keys(Keys.RETURN)
            assert "perfil/" in driver.current_url
            time.sleep(2)

            home_btn = driver.find_element(By.NAME, "home_btn")
            home_btn.send_keys(Keys.RETURN)
            assert "home/" in driver.current_url
            time.sleep(2)

        decoy_publication = True
        
        
        
class T4viewPublicationTest(LiveServerTestCase):
    def testForm(self):
        global logged_in, decoy_publication
        wait = WebDriverWait(driver, 10)
        
        
        print(f"///////////////////logged: {logged_in}")
        print(f"///////////////////decoy_publication: {decoy_publication}")
        
        if logged_in == False:
            #login
            
            # options = Options()
            # options.add_argument('--headless')
            #driver = webdriver.Chrome(options=options)
            
            # driver.get("http://127.0.0.1:8000/")
            
            
            # username = driver.find_element(By.NAME, "username")
            # password = driver.find_element(By.NAME, "password")
            # submit_btn = driver.find_element(By.ID, "login1")
            
            
            # username.send_keys("teste")
            # password.send_keys("senha1234")
            # submit_btn.send_keys(Keys.RETURN)
            
            #logged_in = True
            
            
            T2loginFormTest.testForm(self)
        
        if    decoy_publication == False:
            T3addPublicationTest.testForm(self)
        
        driver.get("http://127.0.0.1:8000/home/")
        time.sleep(1)
        
        
        viewFeed_btn = driver.find_element(By.NAME, "view_feed")
        
        viewFeed_btn.send_keys(Keys.RETURN)
        assert "feed/" in driver.current_url
        time.sleep(2)
        
        
        driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(0.3)
        driver.execute_script("window.scrollTo(0, 900)")
        time.sleep(0.3)
        driver.execute_script("window.scrollTo(0, 1250)")
        time.sleep(0.3)
        #driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(4)
        
        
        category_btn = driver.find_element(By.NAME, "-newProductCategory_btn")
        
        category_btn.send_keys(Keys.RETURN)
        assert "categoria/" in driver.current_url
        time.sleep(3)
        
        
        viewPub_btn = driver.find_element(By.NAME, "newProduct1_btn")
        
        viewPub_btn.send_keys(Keys.RETURN)
        assert "produto/" in driver.current_url
        time.sleep(2)
        
        driver.execute_script("window.scrollTo(0, 550)")
        time.sleep(2)
        
        
        #going back
        return_btn = driver.find_element(By.NAME, "back_btn")
        
        return_btn.send_keys(Keys.RETURN)
        time.sleep(1)
        
        
        return_btn = wait.until(EC.element_to_be_clickable((By.NAME, "back_btn")))
        return_btn.send_keys(Keys.RETURN)
        time.sleep(3)
        
        home_btn = driver.find_element(By.NAME, "home_btn")
        
        home_btn.send_keys(Keys.RETURN)
        
        
        time.sleep(1)
        
        
        
class T5addItensToCartTest(LiveServerTestCase):
    def testForm(self):
        global logged_in, decoy_publication
        wait = WebDriverWait(driver, 10)

        print(f"///////////////////logged: {logged_in}")
        print(f"///////////////////decoy_publication: {decoy_publication}")

        if logged_in == False:
            # Login
            T2loginFormTest.testForm(self)

        if decoy_publication == False:
            T3addPublicationTest.testForm(self)

        driver.get("http://127.0.0.1:8000/home/")
        time.sleep(1)

        profile_btn = driver.find_element(By.NAME, "profile_btn")
        profile_btn.send_keys(Keys.RETURN)
        assert "perfil/" in driver.current_url
        time.sleep(2)

        shoppingCart_btn = driver.find_element(By.NAME, "shoppingCart_btn")
        shoppingCart_btn.send_keys(Keys.RETURN)
        assert "carrinho/" in driver.current_url
        time.sleep(3)

        goShopping_btn = driver.find_element(By.NAME, "goShopping_btn")
        goShopping_btn.send_keys(Keys.RETURN)
        assert "feed/" in driver.current_url
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 1400)")
        time.sleep(1)

        for i in range(3):
            product_btn = driver.find_element(By.NAME, f"newProduct{i+1}_btn")
            product_btn.send_keys(Keys.RETURN)
            assert "produto/" in driver.current_url
            time.sleep(3)

            addToCart_btn = driver.find_element(By.NAME, "addToCart_btn")
            addToCart_btn.send_keys(Keys.RETURN)
            time.sleep(1)

            alert = Alert(driver)
            alert.accept()
            time.sleep(1)

            shoppingCart_btn = driver.find_element(By.NAME, "shoppingCart_btn")
            shoppingCart_btn.send_keys(Keys.RETURN)
            assert "carrinho/" in driver.current_url
            time.sleep(3)

            viewFeed_btn = driver.find_element(By.NAME, "goShopping_btn")
            viewFeed_btn.send_keys(Keys.RETURN)
            assert "feed/" in driver.current_url
            time.sleep(2)

        shoppingCart_btn = driver.find_element(By.NAME, "shoppingCart_btn")
        shoppingCart_btn.send_keys(Keys.RETURN)
        assert "carrinho/" in driver.current_url
        time.sleep(2)

        removeItem_btn = driver.find_element(By.NAME, "removeItem_btn")
        removeItem_btn.send_keys(Keys.RETURN)
        time.sleep(1)

        for i in range(2):
            finalizarCompraItem_btn = driver.find_element(By.NAME, "concluirCompra_btn")
            finalizarCompraItem_btn.send_keys(Keys.RETURN)
            time.sleep(1)    

            alert = Alert(driver)
            alert.accept()
            time.sleep(1)       

        goShopping_btn = driver.find_element(By.NAME, "goShopping_btn")
        goShopping_btn.send_keys(Keys.RETURN)
        assert "feed/" in driver.current_url
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 1400)")
        time.sleep(1)

        home_btn = driver.find_element(By.NAME, "home_btn")
        home_btn.send_keys(Keys.RETURN)
        time.sleep(1)

        viewFeed_btn = driver.find_element(By.NAME, "view_feed")
        viewFeed_btn.send_keys(Keys.RETURN)
        assert "feed/" in driver.current_url
        time.sleep(2)

        
        
        
class T6editProfileTest(LiveServerTestCase):
    def testForm(self):
        global logged_in, decoy_publication
        wait = WebDriverWait(driver, 10)
        
        
        print(f"///////////////////logged: {logged_in}")
        if logged_in == False:
            #login
            T2loginFormTest.testForm(self)
        
        driver.get("http://127.0.0.1:8000/home/")
        time.sleep(1)
        
        
        profile_btn = driver.find_element(By.NAME, "profile_btn")
        
        profile_btn.send_keys(Keys.RETURN)
        assert "perfil/" in driver.current_url
        time.sleep(2)
        
        
        editProfile_btn = driver.find_element(By.NAME, "editProfile_btn")
        
        editProfile_btn.send_keys(Keys.RETURN)
        assert "perfil/editar/" in driver.current_url
        time.sleep(2)
        
        
        username = driver.find_element(By.NAME, "name")
        phone = driver.find_element(By.NAME, "phone")
        description = driver.find_element(By.NAME, "description")  
        save_btn = driver.find_element(By.NAME, "save_btn")
        
        #username.send_keys(Keys.CONTROL + "a")
        #username.send_keys(Keys.DELETE)
        
        #phone.send_keys(Keys.CONTROL + "a")
        #phone.send_keys(Keys.DELETE)
        
        #description.send_keys(Keys.CONTROL + "a")
        #description.send_keys(Keys.DELETE)
        
        username.send_keys("novoNome")
        phone.send_keys("(96)9-9966-9966")
        description.send_keys("descricao do perfil")
        time.sleep(3)
        
        save_btn.send_keys(Keys.RETURN)
        assert "perfil/" in driver.current_url
        time.sleep(4)
        
        
        home_btn = driver.find_element(By.NAME, "home_btn")
        
        home_btn.send_keys(Keys.RETURN)
        assert "home/" in driver.current_url
        time.sleep(1)


class T7finalizarNegociacao(LiveServerTestCase):
    def testForm(self):
        global logged_in, decoy_publication
        wait = WebDriverWait(driver, 10)
        
        
        print(f"///////////////////logged: {logged_in}")
        if logged_in == False:
            #login
            T2loginFormTest.testForm(self)
        
        driver.get("http://127.0.0.1:8000/home/")
        time.sleep(1)

        viewFeed_btn = driver.find_element(By.NAME, "view_feed")
        viewFeed_btn.send_keys(Keys.RETURN)
        assert "feed/" in driver.current_url
        time.sleep(2)

        panelVendedor_btn = driver.find_element(By.NAME, "panelVendedor_btn")
        panelVendedor_btn.send_keys(Keys.RETURN)
        assert "painel_do_vendedor/negociacoes/" in driver.current_url
        time.sleep(3)

        confirnCompra_btn = driver.find_element(By.NAME, "confirmVenda_btn")
        confirnCompra_btn.send_keys(Keys.RETURN)
        time.sleep(2)    

        alert = Alert(driver)
        alert.accept()
        time.sleep(2)

        cancelCompra_btn = driver.find_element(By.NAME, "cancelVenda_btn")
        cancelCompra_btn.send_keys(Keys.RETURN)
        time.sleep(2)    

        alert = Alert(driver)
        alert.accept()
        time.sleep(2)

        shoppingCart_btn = driver.find_element(By.NAME, "shoppingCart_btn")
        shoppingCart_btn.send_keys(Keys.RETURN)
        assert "carrinho/" in driver.current_url
        time.sleep(2)

        notificacaoCompra_btn = driver.find_element(By.NAME, "notificacao_btn")
        notificacaoCompra_btn.send_keys(Keys.RETURN)
        time.sleep(2)  

        notificacaoCompra_btn = driver.find_element(By.NAME, "fecharNotificacao_btn")
        notificacaoCompra_btn.send_keys(Keys.RETURN)
        time.sleep(2)  


class T8editPubTest(LiveServerTestCase):
    def testForm(self):
        global logged_in, decoy_publication
        wait = WebDriverWait(driver, 10)
        
        
        print(f"///////////////////logged: {logged_in}")
        if logged_in == False:
            #login
            T2loginFormTest.testForm(self)
        
        driver.get("http://127.0.0.1:8000/home/")
        time.sleep(1)
        
        
        profile_btn = driver.find_element(By.NAME, "profile_btn")
        
        profile_btn.send_keys(Keys.RETURN)
        assert "perfil/" in driver.current_url
        time.sleep(2)
        
        #
        editPub_btn = driver.find_element(By.ID, "edit_btn")
       
        print("ANTESSS")
        print(driver.current_url)
        editPub_btn.send_keys(Keys.RETURN)
        assert "/editar_publicacao/" in driver.current_url
        print("DEPOISS")
        print(driver.current_url)
        time.sleep(2)
        name = driver.find_element(By.NAME, "productName")
        price = driver.find_element(By.NAME, "productPrice")
        description = driver.find_element(By.NAME, "productDescription")  
        save_btn = driver.find_element(By.NAME, "edit_btn")
        
        name.send_keys("PRODUTO EDITADO")
        price.send_keys("36")
        description.send_keys("DESCRICAO EDITADA")
        time.sleep(3)
        
        
        save_btn.send_keys(Keys.RETURN)
        assert "perfil/" in driver.current_url
        time.sleep(5)
        

        removePub_btn = driver.find_element(By.ID, "remove_btn")
        removePub_btn.send_keys(Keys.RETURN)
        time.sleep(3)

        home_btn = driver.find_element(By.NAME, "home_btn")
        
        home_btn.send_keys(Keys.RETURN)
        assert "home/" in driver.current_url
        time.sleep(1)

        
if __name__ == "__main__":
    unittest.main()