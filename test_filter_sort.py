from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import logging

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestFilterSort(unittest.TestCase):

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

    def test_apply_filter_and_sort(self):
        driver = self.driver

        logging.info("Aplicando filtro 'Price (high to low)'")
        filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        filter_dropdown.click()
        time.sleep(1)  # Espera o dropdown carregar

        filter_option = driver.find_element(By.XPATH, "//option[@value='hilo']")
        filter_option.click()

        logging.info("Filtro 'Price (high to low)' aplicado")

        # Verificar se os produtos estão ordenados corretamente
        first_product_price = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]").text
        second_product_price = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]").text

        logging.info(f"Preço do primeiro produto: {first_product_price}")
        logging.info(f"Preço do segundo produto: {second_product_price}")

        # Converter os preços para float e comparar
        first_price = float(first_product_price.replace('$', ''))
        second_price = float(second_product_price.replace('$', ''))

        try:
            assert first_price > second_price, "Os produtos não estão ordenados corretamente!"
            logging.info("Os produtos estão ordenados corretamente.")
        except AssertionError:
            logging.error("Erro na ordenação: os produtos não estão ordenados corretamente.")

    def tearDown(self):
        logging.info("Encerrando o driver")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

