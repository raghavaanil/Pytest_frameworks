
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
@pytest.mark.regression
@pytest.mark.parametrize("product,exceptedValue",[("iphone","Amazon.in : iphone"),("Oppo","Amazon.in : Oppo"),("Redmi","Amazon.in : figma")])
def test_searchproduct(product,exceptedValue):
    driver.get("https://www.amazon.in/")
    driver.find_element(By.ID,'twotabsearchtextbox').send_keys(product)
    driver.find_element(By.ID,"nav-search-submit-button").click()
    assert exceptedValue==driver.title







