import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AiInterviewTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.aceint.ai/auth/signin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("f2QIlOIS0KbE")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/main/div/div/section[1]/div[2]/div[1]").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_start_interview(self):
        driver = self.driver

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()
        time.sleep(1)

        skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
        skill_input.send_keys("Java")
        skill_input.send_keys(Keys.ENTER)
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
        time.sleep(30)

        self.assertIn("interview", driver.current_url)

    def test_no_job_role_selected(self):
        driver = self.driver

        # Skip job role
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()

        skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
        skill_input.send_keys("Java")
        skill_input.send_keys(Keys.ENTER)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
        time.sleep(3)

        self.assertNotIn("interview", driver.current_url)

    def test_no_domain_selected(self):
        driver = self.driver

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
        # Skip domain
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()

        skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
        skill_input.send_keys("Java")
        skill_input.send_keys(Keys.ENTER)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
        time.sleep(3)

        self.assertNotIn("interview", driver.current_url)

    def test_no_duration_selected(self):
        driver = self.driver

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
        # Skip duration
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()

        skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
        skill_input.send_keys("Java")
        skill_input.send_keys(Keys.ENTER)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
        time.sleep(3)

        self.assertNotIn("interview", driver.current_url)

    def test_no_difficulty_selected(self):
        driver = self.driver

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
        # Skip difficulty

        skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
        skill_input.send_keys("Java")
        skill_input.send_keys(Keys.ENTER)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
        time.sleep(3)

        self.assertNotIn("interview", driver.current_url)

    def test_no_skill_entered(self):
        driver = self.driver

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()
        # No skill entered

        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
        time.sleep(3)

        self.assertNotIn("interview", driver.current_url)

if __name__ == "__main__":
    unittest.main()