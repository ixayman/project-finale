from enum import Enum
from infra.secret_handler import SecretHandler

secret = SecretHandler.load_from_file()


class SpotifyConfig(Enum):
    CLIENT_ID = secret['client_id']
    CLIENT_SECRET = secret['client_secret']
    REDIRECT_URI = 'http://localhost:8000/callback'
    AUTH_URL = 'https://accounts.spotify.com/authorize'
    TOKEN_URL = 'https://accounts.spotify.com/api/token'
    USER_PROFILE_URL = 'https://api.spotify.com/v1/me'


class SpotifyScopes(Enum):
    USER_READ_PRIVATE = "user-read-private"
    USER_READ_EMAIL = "user-read-email"
    PLAYLIST_READ_PRIVATE = "playlist-read-private"
    STREAMING = "streaming"
    USER_READ_PLAYBACK_STATE = "user-read-playback-state"
    USER_MODIFY_PLAYBACK_STATE = "user-modify-playback-state"
    USER_READ_CURRENTLY_PLAYING = "user-read-currently-playing"
    USER_READ_RECENTLY_PLAYED = "user-read-recently-played"
    USER_TOP_READ = "user-top-read"
    APP_REMOTE_CONTROL = "app-remote-control"
    USER_LIBRARY_READ = "user-library-read"
    USER_LIBRARY_MODIFY = "user-library-modify"
    USER_FOLLOW_READ = "user-follow-read"
    USER_FOLLOW_MODIFY = "user-follow-modify"
    PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"
    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"
