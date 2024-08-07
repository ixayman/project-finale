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

    def get_liked_songs(self):
        return self.api.get_request(self.config['api-url'] + 'me/tracks',
                                    headers={'Authorization': 'Bearer ' + self.secret['access_token']})

    @staticmethod
    def check_item_in_playlist(response, id):
        for item in response['items']:
            if item['track']['id'] == id:
                return True
        return False

    def create_playlist(self, name, description, public=False):
        playlist_body = Playlist(name, description, public).to_json()
        return self.api.post_request(self.config['api-url'] + 'users/' + self.secret['user_id'] + '/playlists',
                                     headers={'Authorization': 'Bearer ' + self.secret['access_token']},
                                     body=playlist_body).json()

    def delete_playlist(self, id):
        return self.api.delete_request(self.config['api-url'] + f'playlists/{id}/followers',
                                       headers={'Authorization': 'Bearer ' + self.secret['access_token']})

    def change_playlist_details(self, id, name, description, public):
        playlist_body = Playlist(name, description, public).to_json()
        return self.api.put_request(self.config['api-url'] + f'playlists/{id}',
                                    headers={'Authorization': 'Bearer ' + self.secret['access_token']},
                                    body=playlist_body).json()

    def rearrange_playlist_items(self, id, uris):
        return self.api.post_request(self.config['api-url'] + f'playlists/{id}/tracks',
                                     headers={'Authorization': 'Bearer ' + self.secret['access_token']},
                                     body={'uris': uris}).json()

    def get_playlist_items(self, id):
        return self.api.get_request(self.config['api-url'] + f'playlists/{id}/tracks',
                                    headers={'Authorization': 'Bearer ' + self.secret['access_token']})

    def remove_track_from_playlist(self, playlist_id, track_id):
        body = {
            'tracks': [
                {
                    "uri": f"spotify:track:{track_id}"
                }
            ]
        }
        body = json.dumps(body)
        return self.api.delete_request(self.config['api-url'] + f'playlists/{playlist_id}/tracks',
                                       headers={'Authorization': 'Bearer ' + self.secret['access_token']},
                                       body=body)
