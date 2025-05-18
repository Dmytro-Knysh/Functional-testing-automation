import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(), options=Options())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")

        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))

    def tearDown(self):
        self.driver.quit()

    def test_logout(self):
        self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']"))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        self.assertIn("login", self.driver.current_url.lower())
