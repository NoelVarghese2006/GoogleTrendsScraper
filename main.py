import httpx
import json
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options to run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")
# This is temporary
chrome_options.add_argument("--incognito")
# Pass the Service object to the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://trends.google.com")
time.sleep(10)
driver.maximize_window()
# driver.get("https://google.com")
search_bar = driver.find_element(By.CSS_SELECTOR, '.Fgl6fe-fmcmS-wGMbrd')
info = input("Enter something you would like to know: ")
search_bar.clear()
search_bar.send_keys(info)
explore_button = driver.find_element(By.CSS_SELECTOR, '.Qt4Qjb')
explore_button.click()
time.sleep(1000)