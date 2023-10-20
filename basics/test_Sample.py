import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
@pytest.mark.regression
@pytest.mark.order(1)
def test_launch():
    driver.get("https://www.demoblaze.com/")
@pytest.mark.regression
@pytest.mark.order(3)
def test_gettitile():
    print(driver.title)
@pytest.mark.regression
@pytest.mark.order(4)
def test_getcurrenturl():
    print(driver.current_url)
@pytest.mark.regression
@pytest.mark.order(2)
def test_info():
    time.sleep(5)
    print(driver.find_element(By.XPATH,'//a[normalize-space()="Nokia lumia 1520"]').text)

