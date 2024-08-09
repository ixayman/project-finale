from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler


class PlaybackAPI:

    def __init__(self):
        self.config = ConfigProvider.load_from_file()
        self.secret = SecretHandler.load_from_file()
        self.api = APIWrapper()

    def get_currently_playing_track(self):
        return self.api.get_request(self.config['api-url'] + 'me/player/currently-playing',
                                    headers={'Authorization': 'Bearer ' + self.secret['access_token']})
