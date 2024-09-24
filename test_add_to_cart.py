from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import logging

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        logging.info("Iniciando o setup do driver")
        self.driver = webdriver.Chrome()
        logging.info("Acessando o site SauceDemo")
        self.driver.get("https://www.saucedemo.com/")
        self.login()

    def login(self):
        driver = self.driver
        logging.info("Tentando realizar login com o usuário padrão")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verificar se o login foi bem-sucedido
        try:
            assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()
            logging.info("Login bem-sucedido.")
        except AssertionError:
            logging.error("Falha no login. Carrinho não encontrado.")

    def test_add_products_to_cart(self):
        driver = self.driver

        logging.info("Adicionando o primeiro produto ao carrinho (Sauce Labs Backpack)")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Verificar que o produto foi adicionado (ícone do carrinho com 1 item)
        try:
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert cart_badge.text == "1"
            logging.info("Primeiro produto adicionado ao carrinho com sucesso. 1 item no carrinho.")
        except AssertionError:
            logging.error("Erro ao adicionar o primeiro produto. Carrinho não atualizado.")

        logging.info("Adicionando o segundo produto ao carrinho (Sauce Labs Bike Light)")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Verificar que o carrinho agora tem 2 itens
        try:
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert cart_badge.text == "2"
            logging.info("Segundo produto adicionado ao carrinho com sucesso. 2 itens no carrinho.")
        except AssertionError:
            logging.error("Erro ao adicionar o segundo produto. Carrinho não atualizado.")

    def tearDown(self):
        logging.info("Encerrando o driver")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
