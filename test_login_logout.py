from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import logging

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestSauceDemoLoginLogout(unittest.TestCase):

    def setUp(self):
        logging.info("Iniciando o setup do driver")
        self.driver = webdriver.Chrome()
        logging.info("Acessando o site SauceDemo")
        self.driver.get("https://www.saucedemo.com/")

    def test_login_logout(self):
        driver = self.driver

        # Login
        logging.info("Tentando realizar login com o usuário padrão")
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()
        logging.info("Credenciais enviadas, clicando no botão de login")

        # Verificar se o login foi bem-sucedido (presença do carrinho)
        try:
            assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()
            logging.info("Login bem-sucedido. Carrinho encontrado.")
        except AssertionError:
            logging.error("Login falhou. Carrinho não encontrado.")

        # Logout
        logging.info("Iniciando logout")
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        time.sleep(1)  # Espera o menu abrir
        logging.info("Menu aberto. Clicando no botão de logout")
        logout_button = driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()

        # Verificar se o logout foi bem-sucedido (ver se voltou para a página de login)
        try:
            assert driver.find_element(By.ID, "login-button").is_displayed()
            logging.info("Logout bem-sucedido. Página de login exibida.")
        except AssertionError:
            logging.error("Logout falhou. Botão de login não encontrado.")

    def tearDown(self):
        logging.info("Encerrando o driver")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
