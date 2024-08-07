import unittest
from infra.api.entity.spotify_constants import SpotifyConfig
from infra.api.api_wrapper import APIWrapper
from infra.secret_handler import SecretHandler


class TestProfileInfo(unittest.TestCase):

    def setUp(self):
        self.secret = SecretHandler.load_from_file()
        self.api = APIWrapper()
        self.access_token = self.secret['access_token']
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def tearDown(self):
        self.api = None

    def test_get_profile_info(self):
        """Test retrieving the user's profile information."""
        self.response = self.api.get_request(SpotifyConfig.USER_PROFILE_URL.value, headers=self.headers)
        self.assertEqual(self.response.status_code, 200,
                         f"Expected status code 200, got {self.response.status_code}")
        user_profile = self.response.json()
        self.assertEqual(user_profile['id'], self.secret['user_id'], "User ID in response does not match.")
        self.assertEqual(user_profile['email'], self.secret['email'], "User email in response does not match.")
        self.assertEqual(user_profile['country'], self.secret['user_country'],
                         "User country in response does not match.")
        self.assertEqual(user_profile['display_name'], self.secret['user_display_name'],
                         "User display name in response does not match.")


if __name__ == '__main__':
    unittest.main()
