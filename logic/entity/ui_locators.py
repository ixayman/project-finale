from enum import Enum
from tests.entity.test_data import SampleSong, SamplePlaylist


class HomePageLocators(Enum):
    COOKIE_CLOSE_BUTTON = '//div[@id="onetrust-close-btn-container"]//button'

    LOGIN_BUTTON = '//button[@data-testid="login-button"]'
    SIGNUP_BUTTON = '//button[@data-testid="signup-button"]'
    SEARCH_BUTTON = '//a[@aria-label="Search"]'
    SEARCH_FIELD = '//input[@data-testid="search-input"]'
    LIBRARY_LIST = '//p[@data-encore-id="listRowTitle"]'
    CREATE_PLAYLIST_MENU = '//button[@aria-label="Create playlist or folder"]'
    CREATE_PLAYLIST_BUTTON = '//ul[@role="menu"]//li'
    PLAYLIST_TITLE_BUTTON = '//span[@data-testid="entityTitle"]'
    PLAYLIST_TITLE_INPUT = '//input[@data-testid="playlist-edit-details-name-input"]'
    PLAYLIST_EDIT_SAVE_BUTTON = '//button[@data-testid="playlist-edit-details-save-button"]'

    TOP_SEARCH_RESULT = '//div[@data-testid="top-result-card"]'
    SAVE_TO_LIBRARY_BUTTON = '//button[@data-testid="add-button"]'
    MORE_OPTIONS_BUTTON = '//div[@data-testid="action-bar"]//button[@data-testid="more-button"]'
    ADD_TO_PLAYLIST_BUTTON = '//li[@role="presentation"]//span[contains(text(), "Add to playlist")]'
    ADD_TO_TEST_PLAYLIST_BUTTON = f'//button[@role="menuitem"]//span[text()="{SamplePlaylist.name.value}"]'
    RESULT_PLAY_BUTTON = '//div[@data-testid="action-bar-row"]//button[@aria-label="Play"]'
    RESULT_PAUSE_BUTTON = '//div[@data-testid="action-bar-row"]//button[@aria-label="Pause"]'

    TEST_PLAYLIST_BUTTON = f'//div[@aria-labelledby="listrow-title-spotify:playlist:{SamplePlaylist.id.value}"]'
    PLAYLIST_ITEMS = '//div[@data-testid="playlist-tracklist"]//div[@role="row"][@aria-selected]'
    PLAYLIST_ITEM_OPTIONS_BUTTON = './/div//div//button[@data-testid="more-button"]'
    PLAYLIST_ITEM_REMOVE_BUTTON = '//button//span[contains(text(), "Remove from this playlist")]'
    TEST_SONG_IN_LIBRARY_INDICATOR = f'//div[@data-testid="playlist-tracklist"]//a[contains(@href, {SampleSong.id.value})]'

    PROGRESS_BAR = '//div[@data-testid="progress-bar-background"]/div[1]'

    LIKED_LIST_TRACKS = '//div[@role="row"][@aria-selected]//div[@data-testid="tracklist-row"]'
    LIKED_LIST_PLAY_BUTTON = '//button[@aria-label="Play Liked Songs"][@data-encore-id="buttonPrimary"]'
    LIKED_LIST_PAUSE_BUTTON = '//button[@aria-label="Pause Liked Songs"][@data-encore-id="buttonPrimary"]'

