import unittest
from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
from tests.utils import load_cookies
from tests.entity.test_data import SampleSong, SamplePlaylist


class TestAddTrackToPlaylist(unittest.TestCase):

    def setUp(self):
        self.logger = Logger.setup_logger(__name__)
        try:
            self.config = ConfigProvider.load_from_file()
            self.logger.info("-" * 26)  # Separator line at the start of each test run
            self.logger.info("Loading configuration")
            self.browser = BrowserWrapper()
            self.driver = self.browser.get_driver(self.config, "home_page")
            self.home_page = HomePage(self.driver)
            load_cookies(self.driver, self.config)
            self.playlist_api = PlaylistAPI()
        except Exception as e:
            self.logger.error("Error during setup: %s", str(e))
            raise

    def tearDown(self):
        try:
            self.playlist_api.remove_track_from_playlist(SamplePlaylist.id.value, SampleSong.id.value)
        except Exception as e:
            self.logger.error("Error during teardown: %s", str(e))
        finally:
            self.browser.close_driver()
            self.playlist_api = None

    def test_add_track_to_playlist(self):
        self.logger.info("Starting test: Add Track to Playlist")
        self.home_page.click_search_button()
        self.home_page.insert_in_search_field(SampleSong.name.value + ' ' + SampleSong.artist.value)
        self.home_page.click_top_search_result()
        self.home_page.click_more_options_button()
        self.home_page.hover_on_add_to_playlist_button()
        self.home_page.click_test_playlist_button()
        response = self.playlist_api.get_playlist_items(SamplePlaylist.id.value)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertTrue(self.playlist_api.check_item_in_playlist(response.json(), SampleSong.id.value))
