import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class StandardPlanSubscribeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login()

    def login(self):
        driver = self.driver
        driver.get("https://demo.aceint.ai/auth/signin")
        time.sleep(2)

        # Login with valid credentials
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("atulthakre511@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
        time.sleep(3)

        # Go to pricing page
        driver.get("https://demo.aceint.ai/pricing")
        time.sleep(3)

    def test_click_subscribe_standard_plan(self):
        driver = self.driver
        found = False

        # Find all pricing cards
        cards = driver.find_elements(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/div/div[2]")

        for card in cards:
            try:
                title = card.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]").text
                if "Standard Plan" in title:
                    if "Subscribe Now" in card.text:
                        found = True
                        print("✅ 'Subscribe Now' button found in Standard Plan.")
                        card.screenshot("standard_plan_subscribe_found.png")

                        # Click the button
                        subscribe_button = card.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div[2]/div/div[2]/div[3]/button").click()
                        #subscribe_button.click()
                        time.sleep(3)

                        # Validate redirection or success
                        current_url = driver.current_url
                        print(f"📍 Redirected to: {current_url}")
                        driver.save_screenshot("standard_plan_after_click.png")

                        self.assertNotEqual(current_url, "https://demo.aceint.ai/pricing", 
                                            "❌ Clicking 'Subscribe Now' did not redirect.")
                    else:
                        print("❌ 'Subscribe Now' button missing in Standard Plan.")
                        card.screenshot("standard_plan_subscribe_missing.png")
                    break
            except Exception as e:
                print(f"Error while checking card: {e}")

        self.assertTrue(found, "❌ Standard Plan or Subscribe Now button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
