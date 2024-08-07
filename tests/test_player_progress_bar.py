import time
import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from infra.utils import generate_random_float
from logic.api.playback_api import PlaybackAPI
from logic.ui.home_page import HomePage
from tests.entity.test_data import SampleSong

from tests.utils import load_cookies


class TestPlayerProgressBar(unittest.TestCase):

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
            self.playback_api = PlaybackAPI()
            self.home_page.click_cookie_close_button()
            self.home_page.click_search_button()
            self.home_page.insert_in_search_field(SampleSong.name.value + ' ' + SampleSong.artist.value)
            self.home_page.click_top_search_result()
            self.home_page.click_result_play_button()
            self.home_page.click_result_pause_button()
        except Exception as e:
            self.logger.error("Error during setup: %s", str(e))
            raise

    def tearDown(self):
        self.browser.close_driver()
        self.playback_api = None

    def test_adjust_progress_bar(self):
        self.logger.info("Starting test: Move Progress Bar")
        # arrange
        offset_percentage = generate_random_float(0, 1)
        print(f"Offset percentage: {offset_percentage}")
        timestamp = SampleSong.duration.value * offset_percentage
        # act
        self.home_page.move_progress_bar(offset_percentage)
        response = self.playback_api.get_currently_playing_track()
        # assert
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        print(response.json())
        self.assertAlmostEqual(response.json()['progress_ms'], timestamp, delta=1000,
                               msg=f"Expected progress within 1 second of {timestamp} ms,"
                                   f" got {response.json()['progress_ms']} ms")
