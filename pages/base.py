import globals
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    """
    Class which describe common locators and methods for all pages
    """
    def __init__(self, driver):
        """
        Constructor for Base page
        :param driver:
        """
        self.driver = driver
        self.base_url = globals.BASE_URL

    def find_element(self, locator, time=10):
        """
        Common method for finding element on the page by the locator
        :param locator:
        :param time:
        :return:
        """
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Common method for finding elements on the page by the locator
        :param locator:
        :param time:
        :return:
        """
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        """
        Common method to navigate to the home page
        :return:
        """
        return self.driver.get(self.base_url)