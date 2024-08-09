import unittest

from infra.logger import Logger
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler
from infra.ui.browser_wrapper import BrowserWrapper
from infra.utils import generate_random_string
from logic.ui.home_page import HomePage
from logic.ui.login_page import LoginPage
from logic.api.user_api import UserAPI


class TestLogin(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test case."""
        self.logger = Logger.setup_logger(__name__)
        try:
            self.config = ConfigProvider.load_from_file()
            self.secret = SecretHandler.load_from_file()
            self.logger.info("-" * 26)
            self.logger.info("Loading configuration")
            self.browser = BrowserWrapper()
            self.driver = self.browser.get_driver(self.config, "home_page")
            self.home_page = HomePage(self.driver)
            self.logger.info("Browser opened")
            self.user_api = UserAPI()
        except Exception as e:
            self.logger.error(f"Error in setUp: {e}")
            raise

    def tearDown(self):
        """Clean up the test environment after each test case."""
        try:
            self.browser.close_driver()
            self.user_api = None
        except Exception as e:
            self.logger.error(f"Error in tearDown: {e}")
            raise

    def test_login_with_valid_credentials(self):
        """Test logging in with valid credentials."""
        self.home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.secret['email'], self.secret['password'])

        # Verify login was successful by checking the user info API
        response = self.user_api.get_user_info()
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        self.assertEqual(response.data['id'], self.secret['user_id'])

    def test_login_with_invalid_credentials(self):
        """Test logging in with invalid credentials."""
        self.home_page.click_login_button()
        login_page = LoginPage(self.driver)

        # Attempt login with a valid email and random invalid password
        login_page.insert_username(self.secret['email'])
        login_page.insert_password(generate_random_string(8))
        login_page.click_login_button()

        # Verify that an invalid login message is displayed
        self.assertTrue(login_page.check_invalid_login_message())


if __name__ == '__main__':
    unittest.main()
