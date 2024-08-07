from enum import Enum


class HomePageLocators(Enum):
    COOKIE_CLOSE_BUTTON = '//div[@id="onetrust-close-btn-container"]//button'

    LOGIN_BUTTON = '//button[@data-testid="login-button"]'
    SIGNUP_BUTTON = '//button[@data-testid="signup-button"]'
    SEARCH_BUTTON = '//a[@aria-label="Search"]'
    SEARCH_FIELD = '//input[@data-testid="search-input"]'
    LIBRARY_LIST = '//p[@data-encore-id="listRowTitle"]'

    TOP_SEARCH_RESULT = '//div[@data-testid="top-result-card"]'
    SAVE_TO_LIBRARY_BUTTON = '//button[@data-testid="add-button"]'
    MORE_OPTIONS_BUTTON = '//div[@data-testid="action-bar"]//button[@data-testid="more-button"]'
    ADD_TO_PLAYLIST_BUTTON = '//li[@role="presentation"]//span[contains(text(), "Add to playlist")]'
    RESULT_PLAY_BUTTON = '//div[@data-testid="action-bar-row"]//button[@aria-label="Play"]'
    RESULT_PAUSE_BUTTON = '//div[@data-testid="action-bar-row"]//button[@aria-label="Pause"]'
    TEST_PLAYLIST_BUTTON = '//li[@role="presentation"]//span[contains(text(), "test Playlist")]'

    PLAYLIST_ITEMS = '//div[@data-testid="playlist-tracklist"]//div[@aria-rowindex]'

    PROGRESS_BAR = '//div[@data-testid="progress-bar-background"]/div[1]'
