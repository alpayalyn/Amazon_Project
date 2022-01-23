import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class Setup:
    def __init__(self):
        driver_location = "/usr/bin/chromedriver"
        binary_location = "/usr/bin/google-chrome"
        option = webdriver.ChromeOptions()
        option.binary_location = binary_location
        self.driver = webdriver.Chrome(executable_path=driver_location, options=option)
        self.driver.maximize_window()

