import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
from tests.entity.test_data import SamplePlaylist, SampleSong
from tests.utils import load_cookies


class TestRemoveTrackFromPlaylist(unittest.TestCase):

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
            self.logger.info("Browser opened")
            load_cookies(self.driver, self.config)
            self.logger.info("Cookies loaded")
            self.playlist_api = PlaylistAPI()
            self.playlist_api.add_track_to_playlist(SamplePlaylist.id.value, SampleSong.id.value)
        except Exception as e:
            self.logger.error(f"Error in setUp: {e}")
            raise

    def tearDown(self):
        """Clean up the test environment after each test case."""
        try:
            self.playlist_api.remove_track_from_playlist(SamplePlaylist.id.value, SampleSong.id.value)
            self.playlist_api = None
            self.browser.close_driver()
        except Exception as e:
            self.logger.error(f"Error in tearDown: {e}")
            raise

    def test_remove_track_from_playlist(self):
        """Test removing a track from a playlist."""
        self.logger.info("Starting test: Remove track from playlist")

        # Simulate user interactions to remove a track
        self.home_page.click_cookie_close_button()
        self.home_page.click_test_playlist_button()
        playlist_items = self.home_page.get_playlist_items()
        self.home_page.click_playlist_item_options_button(playlist_items[-1])
        self.home_page.click_playlist_item_remove_button()

        # Verify track removal via API
        response = self.playlist_api.get_playlist_items(SamplePlaylist.id.value)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertFalse(self.playlist_api.check_item_in_playlist(response.data, SampleSong.id.value))
