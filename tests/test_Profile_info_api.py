import unittest
from infra.api.entity.spotify_constants import SpotifyConfig
from infra.api.api_wrapper import APIWrapper
from infra.secret_handler import SecretHandler
from infra.logger import Logger


class TestProfileInfo(unittest.TestCase):

    def setUp(self):
        """Set up the API client and authentication for the test."""
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("-" * 26)
        self.logger.info("Loading configuration")
        self.secret = SecretHandler.load_from_file()
        self.api = APIWrapper()
        self.access_token = self.secret['access_token']
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def tearDown(self):
        """Clean up resources after each test."""
        self.api = None

    def test_get_profile_info(self):
        """Test retrieving the user's profile information."""

        self.logger.info("Starting test: Get profile information")
        self.response = self.api.get_request(SpotifyConfig.USER_PROFILE_URL.value,
                                             headers=self.headers)
        self.assertEqual(self.response.status_code, 200,
                         f"Expected status code 200, got {self.response.status_code}")

        user_profile = self.response.data

        # Validate profile information
        self.assertEqual(user_profile['id'], self.secret['user_id'], "User ID in response does not match.")
        self.assertEqual(user_profile['email'], self.secret['email'], "User email in response does not match.")
        self.assertEqual(user_profile['country'], self.secret['user_country'],
                         "User country in response does not match.")
        self.assertEqual(user_profile['display_name'], self.secret['user_display_name'],
                         "User display name in response does not match.")


if __name__ == '__main__':
    unittest.main()
