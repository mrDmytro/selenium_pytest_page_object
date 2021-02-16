from pages.base import Base
from selenium.webdriver.common.by import By


class Google(Base):
    """
    Class which describe locators and methods for Google Home page
    """
    def __init__(self, driver):
        """
        Constructor for the Google page
        :param driver:
        """
        super().__init__(driver)
        self.field_search_input = By.CSS_SELECTOR, '.gLFyf'
        self.button_submit = By.CLASS_NAME, 'gNO89b'

    def fill_search_input_filed(self, text):
        return self.find_element(self.field_search_input).send_keys(text)

    def click_submit_button(self):
        return self.find_element(self.button_submit).click()
