import pytest as pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from pytest_html_reporter import  attach

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_launch():
    driver.get("https://www.demoblaze.com/index.html")
    print(driver.title)
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[normalize-space()='Nokia lumia 1520']").click()
    time.sleep(3)
    assert driver.find_element(By.XPATH,'//h2[@class="name"]').text == "Nokia lumia 1080", "Mis match of title"
    attach(data=driver.get_screenshot_as_png())

    time.sleep(3)





