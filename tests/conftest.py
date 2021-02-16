import pytest
import time
from selenium import webdriver
import globals


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=globals.CHROME_DRIVER)
    time.sleep(2)
    yield driver
    driver.quit()
