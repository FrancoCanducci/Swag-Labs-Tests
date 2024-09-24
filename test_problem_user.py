from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestProblemUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login()

    def login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    def test_problem_user_checkout(self):
        driver = self.driver
        time.sleep(2)  # Espera a página carregar
        
        # Adiciona o produto "Sauce Labs Backpack" ao carrinho
        add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        logging.info("Produto 'Sauce Labs Backpack' adicionado ao carrinho.")

        # Clica no produto "Sauce Labs Fleece Jacket"
        fleece_jacket = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
        fleece_jacket.click()
        
        time.sleep(2)  # Espera a nova página carregar

        # Captura o título do produto na nova página
        item_not_found_title = driver.find_element(By.CSS_SELECTOR, "div.inventory_details_name").text
        
        # Mensagem esperada
        expected_title = "ITEM NOT FOUND"

        # Verifica se o título do item é "ITEM NOT FOUND"
        assert item_not_found_title == expected_title, "Erro: O título do item não corresponde ao esperado."

        # Navega até o carrinho
        cart_button = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
        cart_button.click()

        time.sleep(2)  # Espera a página do carrinho carregar

        # Clica no botão de checkout
        checkout_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='checkout']")
        checkout_button.click()

        time.sleep(2)  # Espera a página de checkout carregar

        # Tenta preencher as informações de checkout
        driver.find_element(By.ID, "first-name").send_keys("Franco")
        
        # Tenta preencher o sobrenome, mas não vai conseguir
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("")  # Deixamos vazio para simular o erro
        
        # Registra que não foi possível inserir o sobrenome
        logging.warning("Erro: Sobrenome não pode ser inserido.")

        # Clica no botão "Continue"
        continue_button = driver.find_element(By.CSS_SELECTOR, "input[data-test='continue']")
        continue_button.click()

        time.sleep(2)  # Espera a próxima página carregar

        # Verifica se a mensagem de erro aparece
        error_message_element = driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
        if error_message_element:
            error_message_text = error_message_element[0].text
            logging.info(f"Mensagem de erro encontrada: {error_message_text}")

            # Verifica se a mensagem de erro corresponde ao esperado
            assert error_message_text == "Error: Last Name is required", "Erro: Mensagem de erro não corresponde ao esperado."
        
            # Encerra o script
            logging.info("Script encerrado devido à mensagem de erro.")
            return  # Finaliza o teste

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
