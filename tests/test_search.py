import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from tests.entity.test_data import SampleSong
from tests.utils import load_cookies


class TestSearch(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test case."""
        try:
            self.logger = Logger.setup_logger(__name__)
            self.config = ConfigProvider.load_from_file()
            self.logger.info("-" * 26)
            self.logger.info("Loading configuration")
            self.browser = BrowserWrapper()
            self.driver = self.browser.get_driver(self.config, "home_page")
            self.home_page = HomePage(self.driver)
            load_cookies(self.driver, self.config)
        except Exception as e:
            self.logger.error(f"Error in setUp: {e}")
            raise

    def tearDown(self):
        """Clean up the test environment after each test case."""
        try:
            self.browser.close_driver()
        except Exception as e:
            self.logger.error(f"Error in tearDown: {e}")
            raise

    def test_search_specific_song(self):
        """Test searching for a specific song by name and artist."""
        self.logger.info("Starting test: Search for a specific song")
        # act
        self.home_page.click_search_button()
        self.home_page.insert_in_search_field(SampleSong.name.value + ' ' + SampleSong.artist.value)
        result = self.home_page.get_top_search_result()
        # assert
        self.assertIn(SampleSong.name.value, result, f"Expected {SampleSong.name.value} in search result")
        self.assertIn(SampleSong.artist.value, result, f"Expected {SampleSong.artist.value} in search result")
