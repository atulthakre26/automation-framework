import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.aceint.ai/auth/signin")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/button/div").click()
    time.sleep(2)
    yield driver
    driver.quit()

def test_start_interview(driver):
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

    assert "interview" in driver.current_url

def test_no_job_role_selected(driver):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/select/option[4]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/select/option[3]").click()

    skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/button")
    skill_input.send_keys("Java")
    skill_input.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
    time.sleep(3)

    assert "interview" not in driver.current_url

def test_no_domain_selected(driver):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()

    skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
    skill_input.send_keys("Java")
    skill_input.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
    time.sleep(3)

    assert "interview" not in driver.current_url

def test_no_duration_selected(driver):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()

    skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/button")
    skill_input.send_keys("Java")
    skill_input.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
    time.sleep(3)

    assert "interview" not in driver.current_url

def test_no_difficulty_selected(driver):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()

    skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[5]/div/div/input")
    skill_input.send_keys("Java")
    skill_input.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
    time.sleep(3)

    assert "interview" not in driver.current_url

def test_no_skill_entered(driver):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[1]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[2]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[3]/select/option[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[4]/select/option[3]").click()

    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/label[6]/button").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/form/button").click()
    time.sleep(3)

    assert "interview" not in driver.current_url
