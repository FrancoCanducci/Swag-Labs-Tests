from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import logging

class TestSauceDemoCheckout(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Iniciando o driver e abrindo o site")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login()

    def login(self):
        driver = self.driver
        logging.info("Fazendo login no site")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    def test_checkout_flow(self):
        driver = self.driver

        # Adicionar produtos ao carrinho
        logging.info("Adicionando produtos ao carrinho")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Verificar que o carrinho tem 2 itens
        logging.info("Verificando quantidade de itens no carrinho")
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "2", "Carrinho não tem a quantidade esperada de itens"

        # Clicar no ícone do carrinho
        logging.info("Clicando no ícone do carrinho")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verificar que os produtos estão no carrinho
        logging.info("Verificando se os produtos estão no carrinho")
        product1_in_cart = driver.find_element(By.ID, "item_4_title_link").is_displayed()
        product2_in_cart = driver.find_element(By.ID, "item_0_title_link").is_displayed()
        assert product1_in_cart and product2_in_cart, "Nem todos os produtos estão no carrinho"
       

        # Clicar no botão de checkout
        logging.info("Clicando no botão de checkout")
        driver.find_element(By.ID, "checkout").click()

        # Preencher o formulário de checkout
        logging.info("Preenchendo o formulário de checkout")
        driver.find_element(By.ID, "first-name").send_keys("Franco")
        driver.find_element(By.ID, "last-name").send_keys("Canducci")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

        # Clicar em continuar
        logging.info("Clicando em continuar")
        driver.find_element(By.ID, "continue").click()

        # Clicar em finalizar compra
        logging.info("Finalizando a compra")
        driver.find_element(By.ID, "finish").click()


        logging.info("Fluxo de checkout concluído")

    def tearDown(self):
        logging.info("Encerrando o driver")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
