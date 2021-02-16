import time
from pages.google import Google
from pages.google_search import GoogleSearch


class TestMyFirstPageObject:
    """
    Class which test our search functionality
    """
    def test_my_test(self, browser):
        """
        Check input text end find first expected site name
        :param browser:
        :return:
        """
        google = Google(browser)
        search = GoogleSearch(browser)
        google.go_to_site()
        google.fill_search_input_filed('selenium webdriver pytest')
        time.sleep(2)
        google.click_submit_button()
        time.sleep(2)
        titles = search.get_first_site_name()
        time.sleep(2)

        assert titles == 'Легкое веб-тестирование с Python, Pytest и Selenium ...', f"The text doesn't match the actual {titles} "
