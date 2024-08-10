import time

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler


class PlaybackAPI:

    def __init__(self):
        self.config = ConfigProvider.load_from_file()
        self.secret = SecretHandler.load_from_file()
        self.api = APIWrapper()
        self.headers = {
            'Authorization': 'Bearer ' + self.secret['access_token']
        }

    def get_currently_playing_track(self):
        return self.api.get_request(self.config['api-url'] + 'me/player/currently-playing',
                                    headers=self.headers)

    def get_recently_played_tracks(self):
        return self.api.get_request(self.config['api-url'] + 'me/player/recently-played',
                                    headers=self.headers)

    def get_playback_state(self):
        time.sleep(3)
        return self.api.get_request(self.config['api-url'] + 'me/player',
                                    headers=self.headers)

    def start_playback(self):
        return self.api.put_request(self.config['api-url'] + 'me/player/play',
                                    headers=self.headers)

    def pause_playback(self):
        return self.api.put_request(self.config['api-url'] + 'me/player/pause',
                                    headers=self.headers)

    def next_track(self):
        return self.api.post_request(self.config['api-url'] + 'me/player/next',
                                     headers=self.headers)

    def previous_track(self):
        return self.api.post_request(self.config['api-url'] + 'me/player/previous',
                                     headers=self.headers)

    def set_repeat_state(self, state):
        return self.api.put_request(self.config['api-url'] + f'me/player/repeat?state={state}',
                                    headers=self.headers)

    def set_playback_volume(self, volume):
        return self.api.put_request(self.config['api-url'] + f'me/player/volume?volume_percent={volume}',
                                    headers=self.headers)

    def add_track_to_queue(self, track_id):
        return self.api.post_request(self.config['api-url'] + f'me/player/queue?uri=spotify:track:{track_id}',
                                     headers=self.headers)

    def get_user_queue(self):
        time.sleep(2)
        return self.api.get_request(self.config['api-url'] + 'me/player/queue',
                                    headers=self.headers)

