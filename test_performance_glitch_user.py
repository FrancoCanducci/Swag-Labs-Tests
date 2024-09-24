from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import logging
import time

# Configuração do logging
logging.basicConfig(level=logging.INFO)

class TestPerformanceGlitchUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login()

    def login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    def test_performance_glitch_user_checkout(self):
        driver = self.driver
        
        # Adiciona produto ao carrinho
        driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        
        # Clica no botão de checkout
        driver.find_element(By.CSS_SELECTOR, "button[data-test='checkout']").click()

        # Preenche o nome
        first_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Franco")

        # Preenche o sobrenome
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Sobrenome")  # Insira o sobrenome desejado aqui

        # Preenche o CEP
        zip_field = driver.find_element(By.ID, "postal-code")
        zip_field.send_keys("14025520")

        # Clica no botão "Continue"
        continue_button = driver.find_element(By.CSS_SELECTOR, "input[data-test='continue']")
        continue_button.click()

        # Clica no botão "Finish"
        finish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='finish']"))
        )
        finish_button.click()

        # Clica no botão "Back Home"
        back_home_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='back-to-products']")
        
        start_time = time.time()  # Marca o tempo inicial
        back_home_button.click()

        # Aguarda a URL mudar para a URL esperada
        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

        elapsed_time = time.time() - start_time  # Calcula o tempo decorrido
        logging.info(f"Tempo para mudar para a página de inventário: {elapsed_time:.2f} segundos")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
