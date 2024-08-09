# Spotify QA Automation Project

***Introduction***

A Python-based automated testing framework for the Spotify web interface, leveraging Selenium for UI interactions and `unittest` for test execution.

This framework is designed to automate the testing of various functionalities such as user login, playlist management, and player controls. It integrates with Spotify's API for deeper interaction and supports Jira for reporting test results, providing a comprehensive solution for quality assurance in Spotify applications.
## Features

- **Automated Testing**: Execute automated test cases for Spotify's web interface using Selenium.
- **Custom Test Selection**: Select specific test files to run.
- **Cookie Management**: Save and load cookies to maintain user sessions across tests.
- **API Interactions**: Perform operations like getting user info, managing playlists, and controlling playback via Spotify's API.
- **Token Refreshing**: Automatically refresh expired access tokens to maintain API session.
- **Report Generation**: Generate XML reports of test results.
- **Jira Integration**: Upload test results to a Jira board using secure tokens.
## Installation

To get started, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ixayman/project-finale.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd project-finale
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```







## Authentication

Ensure you have a valid `client_secret.json` file containing the following credentials:

1. **Spotify Account Access:**
   - `email`: Your Spotify account email.
   - `password`: Your Spotify account password, used for setting up access and managing cookies.

2. **Spotify API Credentials:**
   - `client_id`: Your Spotify API client ID, obtained from the Spotify Developer Dashboard.
   - `client_secret`: Your Spotify API client secret, also from the Spotify Developer Dashboard.

3. **Jira Integration:**
   - If you plan to use Jira for reporting test runs, save your `jira_aio_token` in `client_secret.json`. The project uses the [AIO Tests Jira Plugin](https://www.aiotests.com/) to facilitate this integration.

**Initialize Session with Cookies:**

- Execute the `save_cookies.py` script once to create a `cookies.pkl` file. This file is essential for maintaining user sessions across tests.

**Authenticate with OAuth 2.0:**

- The project utilizes OAuth 2.0 for authenticating with the Spotify API. Run the `spotify_authentication.py` script to obtain and store an access token and refresh token in `client_secret.json`.
## Running Tests

To use the project, execute the main script:

```bash
python main.py
```

- The script will list all available test files in the `tests` directory.
- You can select which test files to run by entering their numbers separated by commas.
- The tests will run using `pytest`, and an XML report will be generated.


## API Reference

For detailed information on how to use the Spotify API with this project, please refer to the official documentation:

[Spotify API Overview](https://developer.spotify.com/documentation/web-api/)

To understand how the project interacts with Jira for test reporting, visit:

[AIO Tests Jira Plugin Documentation](https://tcms.aiojiraapps.com/aio-tcms/aiotcms-static/api-docs/)

## 🚀 About Me

I'm a QA Automation student with a passion for technology and software testing. I enjoy exploring new tools and techniques to improve software quality and efficiency. Through my studies, I have gained experience in automated testing, Selenium, and API testing. I am excited to apply my skills to real-world projects and continue learning in the field of quality assurance.

![Cute Kitten](https://img.freepik.com/free-photo/view-adorable-kitten-inside-house_23-2150758128.jpg?t=st=1723246137~exp=1723249737~hmac=d284a22289a69916188ee1f576ca841071fbd76a0dd7deaf418b85daff0ff252&w=2000)

