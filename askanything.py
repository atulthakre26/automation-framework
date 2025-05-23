import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AskAnythingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get("https://demo.aceint.ai/auth/signin")
        self.sign_in("atulthakre511@gmail.com", "f2QIlOIS0KbE")

    def tearDown(self):
        self.driver.quit()

    def sign_in(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
        # Wait for chat input to be visible
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form/input")))

    def wait_for_response(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(@class,'message')])[last()]")
        ))

    def test_ask_valid_question(self):
        try:
            input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form/input")))
            input_box.send_keys("What is the capital of India ? ")
            input_box.send_keys(Keys.ENTER)

            response = self.wait_for_response()
            self.assertTrue(len(response.text.strip()) > 0)
        except Exception as e:
            self.fail(f"Failed to submit valid question: {e}")

    def test_ask_empty_question(self):
        try:
            input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form/input")))
            input_box.send_keys("")
            input_box.send_keys(Keys.ENTER)

            time.sleep(5)
            responses = self.driver.find_elements(By.XPATH, "//div[contains(@class,'message')]")
            # Check that the number of messages hasn’t increased unexpectedly
            self.assertTrue(len(responses) < 2)
        except Exception as e:
            self.fail(f"Error while testing empty question: {e}")

    def test_ask_gibberish_question(self):
        try:
            input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form/input")))
            input_box.send_keys("asdlkjasd1234!@#$%^&*")
            input_box.send_keys(Keys.ENTER)

            response = self.wait_for_response()
            self.assertTrue(len(response.text.strip()) > 0)
        except Exception as e:
            self.fail(f"Gibberish question failed: {e}")

if __name__ == "__main__":
    unittest.main()
