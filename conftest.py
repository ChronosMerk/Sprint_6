from selenium import webdriver
import pytest


# Инициализировать драйвер Firefox
@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

