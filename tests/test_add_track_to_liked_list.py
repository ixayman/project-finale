import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
from tests.utils import load_cookies
from tests.entity.test_data import SampleSong


class TestAddTrackToLikedList(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test case."""
        self.logger = Logger.setup_logger(__name__)
        try:
            self.config = ConfigProvider.load_from_file()
            self.logger.info("-" * 26)
            self.logger.info("Loading configuration")
            self.browser = BrowserWrapper()
            self.driver = self.browser.get_driver(self.config, "home_page")
            self.home_page = HomePage(self.driver)
            load_cookies(self.driver, self.config)
        except Exception as e:
            self.logger.error("Error during setup: %s", str(e))
            raise

    def tearDown(self):
        """Clean up the test environment after each test case."""
        try:
            # Remove track from liked list to maintain test isolation
            self.home_page.click_save_to_library_button()
        except Exception as e:
            self.logger.error("Error during teardown: %s", str(e))
        finally:
            self.browser.close_driver()
            self.playlist_api = None

    def test_add_track_to_liked_list(self):
        """Test adding a track to the liked list."""
        self.logger.info("Starting test: Add Track to Liked List")

        # Simulate user actions to search and like a track
        self.home_page.click_search_button()
        self.home_page.insert_in_search_field(SampleSong.name.value + ' ' + SampleSong.artist.value)
        self.home_page.click_top_search_result()
        self.home_page.click_save_to_library_button()

        # Verify that the track is added to the liked list
        self.playlist_api = PlaylistAPI()
        response = self.playlist_api.get_liked_songs()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertTrue(self.playlist_api.check_item_in_playlist(response.data, SampleSong.id.value))


if __name__ == '__main__':
    unittest.main()
