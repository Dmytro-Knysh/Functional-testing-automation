import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginInvalid(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)#options=Options()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def tearDown(self):
        self.driver.quit()

    def test_invalid_login(self):
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")

        username_input.send_keys("Admin")
        password_input.send_keys("wrongpassword")
        login_button.click()

        error = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Invalid credentials']")))
        self.assertIn("Invalid credentials", error.text)

if __name__ == "__main__":
    unittest.main()
