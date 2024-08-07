import subprocess
from tests.utils import jira_aio_upload
from infra.secret_handler import SecretHandler
from infra.api.spotify_refresh_token import refresh_access_token


# Function to run pytest and generate XML report
def run_pytest():
    command = ['pytest', '--log-cli-level=INFO', 'tests/test_add_track_to_playlist.py', '--junitxml=report.xml']
    subprocess.run(command)


if __name__ == '__main__':
    # refresh_access_token()
    secret = SecretHandler.load_from_file()
    run_pytest()
    jira_aio_upload(secret['jira_aio_token'], "KAN-CY-Adhoc")
