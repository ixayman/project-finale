from enum import Enum


class HomePageLocators(Enum):
    LOGIN_BUTTON = '//button[@data-testid="login-button"]'
    SIGNUP_BUTTON = '//button[@data-testid="signup-button"]'
    SEARCH_BUTTON = '//a[@aria-label="Search"]'
    SEARCH_FIELD = '//input[@data-testid="search-input"]'
    LIBRARY_LIST = '//p[@data-encore-id="listRowTitle"]'
    TOP_SEARCH_RESULT = '//div[@data-testid="top-result-card"]'
    SAVE_TO_LIBRARY_BUTTON = '//button[@data-testid="add-button"]'
    PLAYLIST_ITEMS = '//div[@data-testid="playlist-tracklist"]//div[@aria-rowindex]'
