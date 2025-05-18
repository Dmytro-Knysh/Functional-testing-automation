import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginEmptyFields(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(), options=Options())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def tearDown(self):
        self.driver.quit()

    def test_login_with_empty_fields(self):
        self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
        errors = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".oxd-input-field-error-message")
        ))
        self.assertGreaterEqual(len(errors), 1)
