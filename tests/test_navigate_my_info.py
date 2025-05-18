import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMyInfoNavigation(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)#options=Options()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.TAG_NAME, "button")

        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()

    def tearDown(self):
        self.driver.quit()

    def test_navigate_to_my_info(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']"))).click()
        header = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
        self.assertIn("Personal Details", header.text)
