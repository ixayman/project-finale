import time
import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
from tests.utils import load_cookies
from tests.entity.test_data import TestSong, TestPlaylist


class TestAddItemToPlaylist(unittest.TestCase):

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
        self.playlist_api.remove_track_from_playlist(TestPlaylist.id.value, TestSong.id.value)
        self.browser.close_driver()

    def test_add_to_playlist(self):
        self.home_page.click_search_button()
        self.home_page.insert_in_search_field(TestSong.name.value + ' ' + TestSong.artist.value)
        self.home_page.click_top_search_result()
        self.home_page.click_more_options_button()
        self.home_page.hover_on_add_to_playlist_button()
        self.home_page.click_test_playlist_button()
        response = self.playlist_api.get_playlist_items(TestPlaylist.id.value)
        self.assertTrue(self.playlist_api.check_item_in_playlist(response, TestSong.id.value))
