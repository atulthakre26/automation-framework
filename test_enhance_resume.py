import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Helper to return full path of resume
def get_resume_path():
    return os.path.abspath(r"C:\Users\HP\Downloads\AtulResume.pdf")

def get_word_path():
    return os.path.abspath(r"C:\Users\HP\Downloads\Prerequisites_.docx_of_concentrix_process[1].docx")

def get_zip_path():
    return os.path.abspath(r"C:\Users\HP\Downloads\security.zip")

def get_png_path():
    return os.path.abspath(r"C:\Users\HP\Downloads\ChatGPT Image Mar 31, 2025, 12_39_39 PM.png")

def get_jpg_path():
    return os.path.abspath(r"C:\Users\HP\Downloads\Pancard (1).jpg")

# Reusable fixture for login and setup
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://demo.aceint.ai/auth/signin")

    # Login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    ).send_keys("atulthakre511@gmail.com")

    driver.find_element(By.NAME, "password").send_keys("987654321")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

    # Wait for dashboard load (resume link visible)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/resume')]"))
    )

    yield driver
    driver.quit()

# ✅ Test: Full resume upload
def test_pdf_resume_file(driver):
    driver.get("https://demo.aceint.ai/resume")

    # Click Enhance Resume popup card to open modal
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div/main/div[2]/div[1]/div/div/div/div/div"))
    ).click()

    # Select Job Role
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Choose job role')]"))
    ).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']"))
    )

    for option in driver.find_elements(By.XPATH, "//div[@role='option']"):
        if "Associate Software Engineer" in option.text:
            option.click()
            break

    # Select Experience
    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Choose experience')]"))
    # ).click()

    # for option in driver.find_elements(By.XPATH, "//div[@role='option']"):
    #     if "0-1 year" in option.text:
    #         option.click()
    #         break

    # Upload resume
    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    upload_input.send_keys(get_resume_path())
    time.sleep(15)

    # Click Proceed
    proceed_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/button[1]"))
    )
    proceed_btn.click()

    # Wait for upload result
    time.sleep(2)
    page_text = driver.page_source.lower()
    assert "uploaded" in page_text or "success" in page_text


def test_word_file(driver):
    driver.get("https://demo.aceint.ai/resume")

    # Click Enhance Resume popup card to open modal
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div/main/div[2]/div[1]/div/div/div/div/div"))
    ).click()

    # Select Job Role
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Choose job role')]"))
    ).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']"))
    )

    for option in driver.find_elements(By.XPATH, "//div[@role='option']"):
        if "Associate Software Engineer" in option.text:
            option.click()
            break

    # Upload resume
    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    upload_input.send_keys(get_word_path())
    time.sleep(3)

    # Click Proceed
    proceed_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/button[1]"))
    )
    proceed_btn.click()

    # Wait for upload result
    time.sleep(5)
    page_text = driver.page_source.lower()
    assert "uploaded" in page_text or "success" in page_text

def test_zip_file(driver):
    driver.get("https://demo.aceint.ai/resume")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/main/div/div/main/div[2]/div[1]/div/div/div/div/div"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Choose job role')]"))
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH,"//div[@role='option']"))
    )

    for option in driver.find_elements(By.XPATH, "//div[@role='option']"):
       if "Associate Software Engineer" in option.text:  
         option.click()
         break


    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@type='file']"))
    )

    upload_input.send_keys(get_zip_path())
    time.sleep(5)

    proceed_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/button[1]"))
    )

    proceed_btn.click()

    time.sleep(3)

    page_text = driver.page_source.lower()

def test_png_file(driver):
    driver.get("https://demo.aceint.ai/resume")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/main/div/div/main/div[2]/div[1]/div/div/div/div/div"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Choose job role')]"))
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH,"//div[@role='option']"))
    )

    for option in driver.find_elements(By.XPATH, "//div[@role='option']"):
       if "Associate Software Engineer" in option.text:  
         option.click()
         break


    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@type='file']"))
    )

    upload_input.send_keys(get_png_path())
    time.sleep(5)

    proceed_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/button[1]"))
    )

    proceed_btn.click()

    time.sleep(3)

    page_text = driver.page_source.lower()

def test_jpg_file(driver):
    driver.get("https://demo.aceint.ai/resume")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div/main/div[2]/div[1]/div/div/div/div/div"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Choose job role')]"))
    ).click()
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH,"//div[@role='option']"))
    )

    for option in driver.find_elements(By.XPATH, "//div[@role='option']"):
       if "Associate Software Engineer" in option.text:  
         option.click()
         break


    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@type='file']"))
    )

    upload_input.send_keys(get_jpg_path())
    time.sleep(5)

    proceed_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/button[1]"))
    )

    proceed_btn.click()

    time.sleep(3)

    page_text = driver.page_source.lower()


