import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_start_interview(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/button").click()
    time.sleep(3)

    driver.save_screenshot("start_interview.png")
