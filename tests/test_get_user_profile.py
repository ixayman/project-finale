import unittest
from infra.api.entity.spotify_constants import SpotifyConfig
from infra.api.api_wrapper import APIWrapper
from infra.secret_handler import SecretHandler


class TestSpotifyAPI(unittest.TestCase):

    def setUp(self):
        secret = SecretHandler.load_from_file()
        self.api = APIWrapper()
        self.access_token = secret['access_token']
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def test_user_profile(self):
        """Test retrieving the user's profile information."""
        response = self.api.get_request(SpotifyConfig.USER_PROFILE_URL.value, headers=self.headers)

        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")

        user_profile = response.json()

        self.assertIn('id', user_profile, "User ID not found in response.")
        self.assertIn('display_name', user_profile, "Display name not found in response.")
        self.assertIn('email', user_profile, "Email not found in response.")

        print("User Profile:", user_profile)


if __name__ == '__main__':
    unittest.main()
