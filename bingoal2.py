from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
import traceback

def get_page():
    url = "https://www.bingoal.be/fr/Sports/Football/WLD/UEFANATLEA#/overview"
    options = Options()
    options.add_argument("--no-sandbox")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.find_element_by_id("[data-league=\"{}\"]".format)
    