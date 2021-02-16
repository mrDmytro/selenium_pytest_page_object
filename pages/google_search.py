from pages.base import Base
from selenium.webdriver.common.by import By


class GoogleSearch(Base):
    """
    Class which describe locators and methods for Google Search page
    """
    def __init__(self, driver):
        """
        Constructor for the Google Search page
        :param driver:
        """
        super().__init__(driver)
        self.titles = By.TAG_NAME, 'h3'

    def get_first_site_name(self):
        return self.find_elements(self.titles)[1].text
