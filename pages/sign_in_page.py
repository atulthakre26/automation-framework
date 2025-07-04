from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://demo.aceint.ai/auth/signin")

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).send_keys("atulthakre511@gmail.com")

        self.driver.find_element(By.NAME, "password").send_keys("987654321")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/button").click()

    # def navigate(self):
    #     self.driver.get("https://demo.aceint.ai/resume")
        

        # Wait for navigation after login
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "https://demo.aceint.ai/resume"))
        # )
