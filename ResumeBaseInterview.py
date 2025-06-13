import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AiInterviewTest(unittest.TestCase):
    def test_start_interview(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.aceint.ai/")
        time.sleep(3)

        # Initialize WebDriverWait
        wait = WebDriverWait(driver, 10)

        driver.get("https://demo.aceint.ai/auth/signin")
        time.sleep(3)

        # --- Login ---
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
        time.sleep(3)

        # --- Click on Technical Interview ---
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/main/div/div/div[1]/div[2]/div/div[1]/div/div").click()
        time.sleep(2)

        # --- Select Interview Type ---
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/select/option[2]").click()
        time.sleep(2)

        # --- Upload Resume ---
        upload_input = wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[@type='file']"
        )))
        upload_input.send_keys("C:/Users/HP/Downloads/AtulResume.pdf")  # Use absolute local path without `file:///`

        time.sleep(10)

        #--- start Interview ---

        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/form/button").click()
        time.sleep(50)

        driver.quit()

if __name__ == "__main__":
    unittest.main()
