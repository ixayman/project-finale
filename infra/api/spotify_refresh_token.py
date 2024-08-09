import requests

from infra.api.entity.spotify_constants import SpotifyConfig
from infra.secret_handler import SecretHandler


def refresh_access_token():
    """Use the refresh token to get a new access token"""
    secret = SecretHandler.load_from_file()
    refresh_token = secret['refresh_token']
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': SpotifyConfig.CLIENT_ID.value,
        'client_secret': SpotifyConfig.CLIENT_SECRET.value
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(SpotifyConfig.TOKEN_URL.value, data=data, headers=headers)
    token_info = response.json()
    new_access_token = token_info.get('access_token')

    # Update the stored access token
    secret['access_token'] = new_access_token
    SecretHandler.save_to_file(secret)
    return new_access_token


if __name__ == '__main__':
    refresh_access_token()
