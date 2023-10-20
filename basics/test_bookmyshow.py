import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
@pytest.mark.smoke
def test_launch():
    driver.get("https://in.bookmyshow.com/")
@pytest.mark.smoke
def test_gettitile():
    print(driver.title)



