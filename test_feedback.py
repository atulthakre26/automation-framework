import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # ✅ Login
        driver.get("https://demo.aceint.ai/auth/signin")
        time.sleep(2)
        driver.save_screenshot("screenshots/before_login.png")

        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver, 20).until(
            EC.url_changes("https://demo.aceint.ai/auth/signin")
        )
        driver.save_screenshot("screenshots/after_login.png")

    except Exception as e:
        driver.save_screenshot("screenshots/login_failed.png")
        raise Exception("❌ Login failed.") from e

    yield driver
    driver.quit()


def test_feedback_modal(driver):
    wait = WebDriverWait(driver, 15)

    try:
        # ✅ Open Feedback Modal
        feedback_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/ul/li[1]/button/span")))
        feedback_btn.click()
        driver.save_screenshot("screenshots/feedback_modal_opened.png")

        # ✅ Select Category
        # dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/button/span")))
        # Select(dropdown).select_by_visible_text("AI Interview")
        # print("✅ Category selected")

        # ✅ Enter Feedback
        textarea = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/textarea")))
        textarea.send_keys("Amazing platform. Helps with mock interviews effectively.")
        print("✅ Feedback entered")

        # ✅ Give Rating (click 4th star)
        stars = driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/button[4]/svg")
        if len(stars) >= 4:
            stars[3].click()
            print("✅ Rating given")
        else:
            raise Exception("❌ Rating stars not found")

        driver.save_screenshot("screenshots/feedback_filled.png")

        # ✅ Click Send
        send_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/button")
        send_btn.click()
        print("✅ Feedback submitted")
        driver.save_screenshot("screenshots/feedback_sent.png")

    except Exception as e:
        driver.save_screenshot("screenshots/feedback_failed.png")
        raise AssertionError("❌ Feedback modal test failed") from e
