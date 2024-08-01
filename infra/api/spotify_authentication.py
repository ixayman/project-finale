import json
import requests
import urllib.parse
import webbrowser
from flask import Flask, request
from entity.spotify_constants import SpotifyConfig, SpotifyScopes
from infra.secret_handler import SecretHandler


# Step 1: Redirect to Spotify's authorization URL
scope = " ".join([scope.value for scope in SpotifyScopes])

params = {
    'client_id': SpotifyConfig.CLIENT_ID.value,
    'response_type': 'code',
    'redirect_uri': SpotifyConfig.REDIRECT_URI.value,
    'scope': scope
}

auth_url_with_params = f"{SpotifyConfig.AUTH_URL.value}?{urllib.parse.urlencode(params)}"
print("Please navigate to this URL to authorize the app:", auth_url_with_params)


# Start a simple Flask server to capture the authorization code
app = Flask(__name__)


@app.route('/callback')
def callback():
    # Step 2: Capture the authorization code from the URL
    auth_code = request.args.get('code')

    # Step 3: Exchange the authorization code for an access token
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': SpotifyConfig.REDIRECT_URI.value,
        'client_id': SpotifyConfig.CLIENT_ID.value,
        'client_secret': SpotifyConfig.CLIENT_SECRET.value
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(SpotifyConfig.TOKEN_URL.value, data=data, headers=headers)
    token_info = response.json()

    # Access token obtained
    access_token = token_info.get('access_token')
    refresh_token = token_info.get('refresh_token')

    # Read existing data from the JSON file

    secret = SecretHandler.load_from_file()

    # Update the data with new tokens
    secret.update({
        "access_token": access_token,
        "refresh_token": refresh_token
    })

    # Write the updated data back to the JSON file
    SecretHandler.save_to_file(secret)

    # Return a response to the browser
    return "Authorization complete! You can close this browser tab."


if __name__ == '__main__':
    # Open the browser automatically
    webbrowser.open(auth_url_with_params)

    # Start the Flask server to listen for the callback
    app.run(port=8000)
