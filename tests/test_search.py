import time
import unittest

from infra.logger import Logger
from infra.utils import generate_random_string
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from tests.utils import load_cookies


class TestSearch(unittest.TestCase):

    def setUp(self):
        """
        """
        self.logger = Logger.setup_logger(__name__)
        self.config = ConfigProvider.load_from_file()
        self.logger.info("-" * 26)  # Separator line at the start of each test run
        self.logger.info("Loading configuration")
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config, "home_page")
        self.home_page = HomePage(self.driver)
        self.logger.info("Browser opened")
        load_cookies(self.driver, self.config)
        self.logger.info("Cookies loaded")

    def tearDown(self):
        self.browser.close_driver()

    def test_search(self):
        self.home_page.click_search_button()
        self.logger.info("Search button clicked")
        self.logger.info("Test completed")
