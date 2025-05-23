import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SignInTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.aceint.ai/auth/signin")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def sign_in(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/form/div[1]/input"))).send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/div[1]/input").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
        time.sleep(3)

    def test_valid_signin(self):
        """Test login with valid email and password"""
        self.sign_in("atulthakre511@gmail.com", "f2QIlOIS0KbE")
        self.assertIn("AceInt", self.driver.title)


    def test_invalid_password(self):
   # """Test login with correct email but incorrect password"""
        self.sign_in("atulthakre511@gmail.com", "wrongpassword123")
        error_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Incorrect') or contains(text(), 'invalid') or contains(text(), 'Invalid')]")
        self.assertTrue(any(e.text.strip() for e in error_elements), "Expected an error message for invalid credentials")


def test_invalid_email(self):
    """Test login with invalid email format"""
    email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/form/div[1]/input")))
    email_input.send_keys("invalidemail")
    email_input.send_keys(Keys.TAB)
    time.sleep(1)
    self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/div[1]/input").send_keys("somepassword")
    self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
    time.sleep(2)
    error_elements = self.driver.find_elements(By.CLASS_NAME, "text-red-500")
    self.assertTrue(len(error_elements) > 0, "Expected an error message for invalid email format")

def test_empty_fields(self):
    """Test login with empty email and password"""
    self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
    time.sleep(2)
    error_elements = self.driver.find_elements(By.CLASS_NAME, "text-red-500")
    self.assertGreater(len(error_elements), 0, "Expected error messages for empty fields")


if __name__ == "__main__":
    unittest.main()
