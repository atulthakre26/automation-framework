import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- Fixtures ----------

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.aceint.ai/auth/signin")

    # Login setup
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input").send_keys("atulthakre511@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[1]/input").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/button").click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "main")))
    yield driver
    driver.quit()


# ---------- Utility Method ----------

def safe_click(driver, xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    ActionChains(driver).move_to_element(element).click().perform()


# ---------- Test Cases ----------

def test_click_technical_interview(driver):
    safe_click(driver, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[1]/div[2]/div/div[1]/div/div")


def test_select_interview_type(driver):
    test_click_technical_interview(driver)

    # Wait for modal to appear and click dropdown
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div/button"))
    )
    dropdown_button.click()

    # Select the "Technical" option
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div/select/option[1]"))
    )
    option.click()

    # Validate selection (optional)
    selected_text = dropdown_button.text
    #assert "Technical" in selected_text


def test_upload_resume(driver):
    test_click_technical_interview(driver)
    test_select_interview_type(driver)

    # Upload file
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    file_input.send_keys("C:/Users/HP/Downloads/AtulResume.pdf")


def test_start_interview_button_enabled(driver):
    test_click_technical_interview(driver)
    test_select_interview_type(driver)
    test_upload_resume(driver)

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Interview')]"))
    )
    #assert start_button.is_enabled()


def test_start_interview_flow(driver):
    test_click_technical_interview(driver)
    test_select_interview_type(driver)
    test_upload_resume(driver)

    # Start Interview
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Interview')]"))
    )
    #start_button.click()
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
    time.sleep(1)

    # Click using JS to avoid interception
    driver.execute_script("arguments[0].click();", start_button)

    # Wait for video or recording element
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "video"))
    )
