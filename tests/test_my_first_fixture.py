import time
from selenium import webdriver
import pytest


class TestMyFirstFixture:

    @pytest.fixture(scope="session")
    def browser(self):
        driver = webdriver.Chrome()
        driver.get('https://google.ua')
        time.sleep(2)
        yield driver
        driver.quit()

    def test_my_test(self, browser):
        field_search_input = browser.find_element_by_css_selector('.gLFyf')
        field_search_input.send_keys('selenium webdriver pytest')
        time.sleep(2)
        button_submit = browser.find_element_by_class_name('gNO89b')
        button_submit.click()
        time.sleep(2)

        titles = browser.find_elements_by_tag_name('h3')

        first_title = titles[1]

        print(first_title.text)
        time.sleep(2)

        assert first_title.text == 'Легкое веб-тестирование с Python, Pytest и Selenium ...', 'The text doesn\'t match the actual'
