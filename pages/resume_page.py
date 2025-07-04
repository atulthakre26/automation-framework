from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ResumePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demo.aceint.ai/resume")

    def select_job_role(self, role_text):
        job_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "jobRole"))
        )
        Select(job_dropdown).select_by_visible_text(role_text)

    def select_experience(self, experience_text):
        exp_dropdown = self.driver.find_element(By.NAME, "experience")
        Select(exp_dropdown).select_by_visible_text(experience_text)

    def upload_resume(self, file_path):
        upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        upload_input.send_keys(file_path)

    def click_proceed(self):
        proceed_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]")
        proceed_btn.click()
        time.sleep(2)
