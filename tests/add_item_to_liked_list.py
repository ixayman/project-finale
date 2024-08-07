import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
from tests.utils import load_cookies
from tests.entity.test_data import TestSong


class TestAddItemToLikedList(unittest.TestCase):

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
        self.playlist_api = PlaylistAPI()

    def tearDown(self):
        self.home_page.click_save_to_library_button()
        self.browser.close_driver()

    def test_add_to_liked_list(self):
        self.home_page.click_search_button()
        self.home_page.insert_in_search_field(TestSong.name.value + ' ' + TestSong.artist.value)
        self.home_page.click_top_search_result()
        self.home_page.click_save_to_library_button()
        response = self.playlist_api.get_liked_songs()
        self.assertTrue(
            self.playlist_api.check_item_in_playlist(response, TestSong.id.value))
