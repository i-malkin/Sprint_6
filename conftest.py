from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver

    driver.quit()
