import time
import unittest
from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from infra.utils import generate_random_string
from logic.ui.home_page import HomePage
from logic.api.playlist_api import PlaylistAPI
from tests.utils import load_cookies


class TestAddTrackToPlaylist(unittest.TestCase):

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
            self.playlist_api = PlaylistAPI()
            self.new_playlist_id = None
        except Exception as e:
            self.logger.error("Error during setup: %s", str(e))
            raise

    def tearDown(self):
        """Clean up the test environment after each test case."""
        try:
            if self.new_playlist_id:
                self.playlist_api.delete_playlist(self.new_playlist_id)
            self.browser.close_driver()
            self.playlist_api = None
        except Exception as e:
            self.logger.error("Error during teardown: %s", str(e))
            raise

    def test_create_custom_name_playlist(self):
        """
          THIS IS A SLOW TEST DUE TO SPOTIFY BACKEND LIMITATIONS
        """

        """ Test creating a playlist with a custom name. """
        self.logger.info("Starting test: Create Playlist")
        new_playlist_name = generate_random_string(8)

        # Simulate user actions to create a playlist
        self.home_page.click_create_playlist_menu()
        self.home_page.click_create_playlist_button()
        self.home_page.click_playlist_title_button()
        self.home_page.insert_in_playlist_title_input(new_playlist_name)
        self.home_page.click_playlist_edit_save_button()

        time.sleep(60)  # Necessary delay to ensure backend updates
        self.home_page.refresh_page()

        # Verify the new playlist is created
        user_playlists = self.playlist_api.get_user_playlists()
        playlist = self.playlist_api.get_playlist_via_name_from_playlists(new_playlist_name, user_playlists.data)
        self.assertTrue(playlist, f"Playlist with name {new_playlist_name} not found in playlists")
        self.new_playlist_id = playlist['id']


if __name__ == '__main__':
    unittest.main()
