
import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.ui.login_page import LoginPage
from logic.api.user_api import UserAPI


class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        """
        self.logger = Logger.setup_logger(__name__)
        self.config = ConfigProvider.load_from_file()
        self.secret = SecretHandler.load_from_file()
        self.logger.info("-" * 26)  # Separator line at the start of each test run
        self.logger.info("Loading configuration")
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config, "home_page")
        self.home_page = HomePage(self.driver)
        self.logger.info("Browser opened")
        self.user_api = UserAPI()

    def tearDown(self):
        self.browser.close_driver()

    def test_login_with_valid_credentials(self):
        self.home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.secret['username'], self.secret['password'])
        response = self.user_api.get_user_info()
        self.assertEqual(response['display_name'], 'Ayman Khalil')

    def test_login_with_invalid_credentials(self):
        self.home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.insert_username(self.secret['username'])
        login_page.insert_password('12345678')
        login_page.click_login_button()
        self.assertTrue(login_page.check_invalid_login_message())

