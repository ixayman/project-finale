import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
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
        self.playlist_api = PlaylistAPI()

    def tearDown(self):
        self.browser.close_driver()

    def test_rearrange_playlist(self):
        self.home_page.click_playlist_from_library('test Playlist')
        self.home_page.drag_and_drop_playlist_item(3, 6)
