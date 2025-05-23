import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.aceint.ai/auth/signup")
        time.sleep(1)

        # --- Enter First Name
        skill_input = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[1]/div[1]/input")
        skill_input.send_keys("Atul")
        time.sleep(1)
        
        # --- Enter Last Name 
        skill_input = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div[1]/div[2]/input")
        skill_input.send_keys("Thakre")
        time.sleep(1)

        # Correct XPath and remove typo
        driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/input").send_keys("pewemat216@pricegh.com")
        driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[3]/div/input").send_keys("123456789")
        driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()

        # Optional: wait for page to load (explicit wait is better)
        time.sleep(5)

        # Validate URL contains 'dashboard' (you may need to adjust this based on actual redirect)
        self.assertIn("dashboard", driver.current_url)

        driver.quit()

if __name__ == "__main__":
    unittest.main()