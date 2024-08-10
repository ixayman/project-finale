from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler


class UserAPI:

    def __init__(self):
        self.config = ConfigProvider.load_from_file()
        self.secret = SecretHandler.load_from_file()
        self.api = APIWrapper()

        self.headers = {
            'Authorization': 'Bearer ' + self.secret['access_token']
        }

    def get_user_info(self):
        return self.api.get_request(self.config['api-url'] + 'me',
                                    headers=self.headers)

    def get_followed_artists(self):
        return self.api.get_request(self.config['api-url'] + 'me/following',
                                    headers=self.headers)

    def follow_artist(self, artist_id):
        return self.api.put_request(self.config['api-url'] + f'me/following?type=artist&ids={artist_id}',
                                    headers=self.headers)

    def unfollow_artist(self, artist_id):
        return self.api.delete_request(self.config['api-url'] + f'me/following?type=artist&ids={artist_id}',
                                       headers=self.headers)

    def check_if_user_follows_artist(self, artist_id):
        return self.api.get_request(self.config['api-url'] + f'me/following/contains?type=artist&ids={artist_id}',
                                    headers=self.headers)

    def check_if_current_user_follows_playlist(self, playlist_id):
        return self.api.get_request(self.config['api-url'] + f'me/playlists/{playlist_id}/contains',
                                    headers=self.headers)
