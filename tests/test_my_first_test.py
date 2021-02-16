import time
from selenium import webdriver


class TestMyFirstTest:
    def test_my_test(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get('https://google.ua')
        time.sleep(2)

        field_search_input = driver.find_element_by_css_selector('.gLFyf')

        field_search_input.send_keys('selenium webdriver pytest')
        time.sleep(2)

        button_submit = driver.find_element_by_class_name('gNO89b')
        button_submit.click()
        time.sleep(2)

        driver.quit()
