import time
import unittest

from infra.config_provider import ConfigProvider
from infra.logger import Logger
from infra.ui.browser_wrapper import BrowserWrapper
from logic.api.playback_api import PlaybackAPI
from logic.ui.home_page import HomePage
from tests.entity.test_data import SampleSong
from tests.utils import load_cookies


class TestPlaybackControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the API client and authentication for the test."""
        try:
            cls.logger = Logger.setup_logger(__name__)
            cls.logger.info("-" * 26)
            cls.logger.info("Loading configuration")
            cls.config = ConfigProvider.load_from_file()
            cls.browser = BrowserWrapper()
            cls.driver = cls.browser.get_driver(cls.config, "home_page")
            cls.home_page = HomePage(cls.driver)
            load_cookies(cls.driver, cls.config)
            cls.driver.get(cls.config['liked_tracks_page'])
            cls.liked_page = HomePage(cls.driver)
            cls.liked_page.click_cookie_close_button()
            cls.liked_page.double_click_liked_list_track()
            cls.playback_api = PlaybackAPI()
        except Exception as e:
            cls.logger.error("Error during setup: %s", str(e))
            raise

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after all tests have run."""
        try:
            cls.playback_api.pause_playback()
            cls.playback_api = None
            cls.browser.close_driver()
        except Exception as e:
            cls.logger.error("Error during teardown: %s", str(e))

    def test_01_pause_playback(self):
        """Test pausing playback."""
        self.logger.info("running test: pause playback")
        self.playback_api.pause_playback()
        response = self.playback_api.get_playback_state()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['is_playing'], False, "Expected is_playing to be False")

    def test_02_start_playback(self):
        """Test starting playback."""
        self.logger.info("running test: start playback")
        self.playback_api.start_playback()
        response = self.playback_api.get_playback_state()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['is_playing'], True, "Expected is_playing to be True")
        print(response.data)

    def test_03_adjust_volume(self):
        """Test adjusting volume."""
        self.logger.info("running test: adjust volume")
        volume = 80
        self.playback_api.set_playback_volume(volume)
        response = self.playback_api.get_playback_state()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['device']['volume_percent'], volume, f"Expected volume_percent to be {volume}")

    def test_04_next_track(self):
        """Test next track."""
        self.logger.info("running test: next track")
        self.playback_api.next_track()
        response = self.playback_api.get_playback_state()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['item']['track_number'], 3, "Expected track_number to be 2")

    def test_05_previous_track(self):
        """Test previous track."""
        self.logger.info("running test: previous track")
        self.playback_api.previous_track()
        response = self.playback_api.get_playback_state()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['item']['track_number'], 2, "Expected track_number to be 1")

    def test_06_repeat_state(self):
        """Test repeat state."""
        self.logger.info("running test: repeat state")
        repeat_state = 'track'
        self.playback_api.set_repeat_state(repeat_state)
        response = self.playback_api.get_playback_state()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['repeat_state'], repeat_state, f"Expected repeat_state to be {repeat_state}")

    def test_07_add_track_to_queue(self):
        """Test adding track to queue."""
        self.logger.info("running test: add track to queue")
        track_id = SampleSong.id.value
        self.playback_api.add_track_to_queue(track_id)
        response = self.playback_api.get_user_queue()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['queue'][0]['name'], f'{SampleSong.name.value}')
