from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from spellchecker import SpellChecker 
import time

# Setup WebDriver (make sure you have chromedriver installed and in PATH)
driver = webdriver.Chrome()  # or use Service(executable_path="path/to/chromedriver")

# Open the website
driver.get("https://demo.aceint.ai")
driver.maximize_window()
time.sleep(5)  # wait for content to load

# Extract visible text from the body
body_text = driver.find_element(By.TAG_NAME, "body").text

# Close the browser
driver.quit()

# Initialize spell checker
spell = SpellChecker()

# Tokenize and clean the text
words = body_text.split()
misspelled = spell.unknown(words)

# Print misspelled words
if misspelled:
    print("Misspelled words found:")
    for word in misspelled:
        print(f" - {word} (did you mean: {spell.correction(word)})")
else:
    print("No spelling mistakes found.")
