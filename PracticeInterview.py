import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AiInterviewTest(unittest.TestCase):
    def test_start_interview(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.aceint.ai/")
        time.sleep(3)
        
        driver.get("https://demo.aceint.ai/auth/signin")
        time.sleep(3)
        # ---Sign In ---
        #driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/a").click()
        
        # --- Login ---
        
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
        time.sleep(3)
        

        # --- Click on Technical Interview  ---
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/button").click()
        time.sleep(2)

        # --- Select Job Role ---   /html/body/div[3]/div/form/label[1]/button
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/select/option[3]").click()

        # --- Select Interview Type ---
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[2]/select/option[3]").click()

        # --- Select Duration ---
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[2]/label[1]/select/option[2]").click()

        # --- Select Difficulty ---
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[2]/label[2]/select/option[2]").click()
       # time.sleep(3)

        # --- Enter Technical Skill ---
        skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[3]/label/div/input")
        skill_input.send_keys("Java")
        skill_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # --- Agree to Terms ---
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[1]/label/button").click()
        time.sleep(1)

        # --- Start Interview ---
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[2]/button").click()

        # --- Wait for redirection ---
        time.sleep(30)
        #driver.find_element(By.XPATH,"/html/body/div/main/div/section[2]/div/div[2]/a").click()
        #time.sleep(25)
        self.assertIn("interview", driver.current_url)

       # driver.quit()

if __name__ == "__main__":
    unittest.main()