import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginSuccess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(), options=Options())
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")
        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()
        dashboard = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        self.assertIn("Dashboard", dashboard.text)
