import json

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler
from logic.entity.playlist import Playlist


class PlaylistAPI:

    def __init__(self):
        self.config = ConfigProvider.load_from_file()
        self.secret = SecretHandler.load_from_file()
        self.api = APIWrapper()

        self.headers = {
            'Authorization': 'Bearer ' + self.secret['access_token']
        }

    def get_liked_songs(self):
        return self.api.get_request(self.config['api-url'] + 'me/tracks', headers=self.headers)

    def remove_track_from_liked_songs(self, id):
        return self.api.delete_request(self.config['api-url'] + f'me/tracks?ids={id}', headers=self.headers)

    def get_user_playlists(self):
        return self.api.get_request(self.config['api-url'] + 'me/playlists', headers=self.headers)

    @staticmethod
    def get_playlist_via_name_from_playlists(playlist_name, playlists):
        for playlist in playlists['items']:
            if playlist['name'] == playlist_name:
                return playlist
        return False

    @staticmethod
    def check_item_in_playlist(playlist, item_id):
        for item in playlist['items']:
            if item['track']['id'] == item_id:
                return True
        return False

    def create_playlist(self, name, description, public=False):
        playlist_body = Playlist(name, description, public).to_json()
        return self.api.post_request(self.config['api-url'] + 'users/' + self.secret['user_id'] + '/playlists',
                                     headers=self.headers,
                                     body=playlist_body)

    def delete_playlist(self, playlist_id):
        return self.api.delete_request(self.config['api-url'] + f'playlists/{playlist_id}/followers',
                                       headers=self.headers)

    def change_playlist_details(self, playlist_id, name, description, public):
        playlist_body = Playlist(name, description, public).to_json()
        return self.api.put_request(self.config['api-url'] + f'playlists/{playlist_id}', headers=self.headers,
                                    body=playlist_body).json()

    def rearrange_playlist_items(self, playlist_id, uris):
        return self.api.post_request(self.config['api-url'] + f'playlists/{playlist_id}/tracks', headers=self.headers,
                                     body={'uris': uris}).json()

    def get_playlist_items(self, playlist_id):
        return self.api.get_request(self.config['api-url'] + f'playlists/{playlist_id}/tracks', headers=self.headers)

    def add_track_to_playlist(self, playlist_id, track_id):
        body = {
            'uris': [
                f"spotify:track:{track_id}"
            ]
        }
        body = json.dumps(body)
        return self.api.post_request(self.config['api-url'] + f'playlists/{playlist_id}/tracks', headers=self.headers,
                                     body=body)

    def remove_track_from_playlist(self, playlist_id, track_id):
        body = {
            'tracks': [
                {
                    "uri": f"spotify:track:{track_id}"
                }
            ]
        }
        body = json.dumps(body)
        return self.api.delete_request(self.config['api-url'] + f'playlists/{playlist_id}/tracks', headers=self.headers,
                                       body=body)
