import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()  # Optional: specify ChromeDriver path if needed
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # ✅ Step 1: Open login page
        driver.get("https://demo.aceint.ai/auth/signin")
        time.sleep(2)
        driver.save_screenshot("screenshots/before_login.png")

        # ✅ Step 2: Fill login form
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # ✅ Step 3: Wait until URL changes (indicating successful login)
        WebDriverWait(driver, 20).until(
            EC.url_changes("https://demo.aceint.ai/auth/signin")
        )
        driver.save_screenshot("screenshots/after_login.png")

    except Exception as e:
        driver.save_screenshot("screenshots/login_failed.png")
        raise Exception("❌ Login failed - please check credentials or page structure.") from e

    yield driver
    driver.quit()


def test_interview_summary_page(driver):
    url = "https://demo.aceint.ai/interview/summary/d0d9c64a-caf7-4718-be72-dd27577a9d7c"
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    driver.save_screenshot("screenshots/summary_loaded.png")

    # List of elements to verify
    elements_to_check = [
        ("//*[contains(text(), 'Video Playback Restricted')]", "Video Restriction Message"),
        ("//*[contains(text(), 'Campus Readiness')]", "Campus Readiness Section"),
        ("//*[contains(text(), 'Overall Score')]", "Overall Score"),
        ("//*[contains(text(), 'Performance Summary')]", "Performance Summary Tab"),
        ("//*[contains(text(), 'Key Strengths')]", "Key Strengths Section"),
        ("//*[contains(text(), 'Areas for Improvement')]", "Areas for Improvement Section"),
        ("//*[contains(text(), 'Concerning Aspects')]", "Concerning Aspects Section"),
        ("//*[contains(text(), 'Transcript')]", "Transcript Button"),
    ]

    for xpath, description in elements_to_check:
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            print(f"✅ Found: {description}")
        except Exception as e:
            driver.save_screenshot(f"screenshots/failed_{description.replace(' ', '_').lower()}.png")
            raise AssertionError(f"❌ Failed to find: {description}")

    driver.save_screenshot("screenshots/interview_summary_passed.png") 
