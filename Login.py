import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SignInTest(unittest.TestCase):
    def test_valid_signin(self):
        driver = webdriver.Chrome()
        driver.get("https://www.hireskilldev.com/auth/signin")
        
        # Enter email
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input").send_keys("atulthakre511@gmail.com")
        #/html/body/div/div/div/form/div[1]/input
        # Enter password
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[1]/input").send_keys("f2QIlOIS0KbE")
        
        # Click sign in button
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/button").click()
        
        # Wait for redirection (use WebDriverWait for better practice)
        time.sleep(5)
        
        # Assert URL contains 'dashboard' after login
        self.assertIn("AI Interview", driver.current_url)
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()
