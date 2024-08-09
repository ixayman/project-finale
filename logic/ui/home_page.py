import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

from infra.ui.base_page import BasePage
from infra.logger import Logger
from logic.entity.ui_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(__name__)
        # Initialize the elements

    def click_cookie_close_button(self):
        """Close the cookie consent banner."""
        try:
            cookie_close_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.COOKIE_CLOSE_BUTTON.value))
            )
            cookie_close_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click the cookie close button: {str(e)}")
            raise

    def click_login_button(self):
        """Click the login button and wait for the login page to load."""
        try:
            login_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.LOGIN_BUTTON.value))
            )
            login_button.click()
            WebDriverWait(self._driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, '//h1[text()="Log in to Spotify"]'))
            )
        except Exception as e:
            self.logger.error(f"Failed to click the login button: {str(e)}")
            raise

    def click_signup_button(self):
        """Click the sign-up button."""
        try:
            signup_button = WebDriverWait(self._driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, HomePageLocators.SIGNUP_BUTTON.value))
            )
            signup_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click the signup button: {str(e)}")
            raise

    def click_playlist_from_library(self, playlist_name):
        """Click on a playlist in the library."""
        try:
            library_list = WebDriverWait(self._driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, HomePageLocators.LIBRARY_LIST.value))
            )
            playlist = WebDriverWait(library_list, 10).until(
                ec.element_to_be_clickable((By.XPATH, f'//span[text()="{playlist_name}"]'))
            )
            self._driver.execute_script("arguments[0].scrollIntoView(true);", playlist)
            ActionChains(self._driver).move_to_element(playlist).click().perform()
            print(f'Clicked on playlist: {playlist.text}')
        except Exception as e:
            self.logger.error(f"Failed to click on playlist {playlist_name}: {str(e)}")
            raise

    def click_create_playlist_menu(self):
        """Click the create playlist menu."""
        try:
            create_playlist_menu = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.CREATE_PLAYLIST_MENU.value))
            )
            create_playlist_menu.click()
        except Exception as e:
            self.logger.error("Failed to click the create playlist menu: %s", str(e))
            raise

    def click_create_playlist_button(self):
        """Click the button to create a new playlist."""
        try:
            create_playlist_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.CREATE_PLAYLIST_BUTTON.value))
            )
            create_playlist_button.click()
        except Exception as e:
            self.logger.error("Failed to click the create playlist button: %s", str(e))
            raise

    def click_playlist_title_button(self):
        """Click the playlist title button."""
        try:
            playlist_title = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.PLAYLIST_TITLE_BUTTON.value))
            )
            playlist_title.click()
        except Exception as e:
            self.logger.error("Failed to click the playlist title button: %s", str(e))
            raise

    def insert_in_playlist_title_input(self, text):
        """Insert text into the playlist title input field."""
        try:
            playlist_title_input = WebDriverWait(self._driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, HomePageLocators.PLAYLIST_TITLE_INPUT.value))
            )
            playlist_title_input.send_keys(text)
        except Exception as e:
            self.logger.error("Failed to insert text into playlist title input: %s", str(e))
            raise

    def click_playlist_edit_save_button(self):
        """Click the save button after editing a playlist."""
        try:
            playlist_edit_save_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.PLAYLIST_EDIT_SAVE_BUTTON.value))
            )
            playlist_edit_save_button.click()
            time.sleep(2)
        except Exception as e:
            self.logger.error("Failed to click the playlist edit save button: %s", str(e))
            raise

    def click_search_button(self):
        """Click the search button."""
        try:
            search_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.SEARCH_BUTTON.value))
            )
            search_button.click()
        except Exception as e:
            self.logger.error("Failed to click the search button: %s", str(e))
            raise

    def insert_in_search_field(self, text):
        """Insert text into the search field."""
        try:
            search_field = WebDriverWait(self._driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, HomePageLocators.SEARCH_FIELD.value))
            )
            search_field.send_keys(text)
        except Exception as e:
            self.logger.error("Failed to insert text into the search field: %s", str(e))
            raise

    def click_top_search_result(self):
        """Click the top search result."""
        try:
            top_search_result = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.TOP_SEARCH_RESULT.value))
            )
            top_search_result.click()
        except Exception as e:
            self.logger.error("Failed to click the top search result: %s", str(e))
            raise

    def get_top_search_result(self):
        """Get the text of the top search result."""
        try:
            top_search_result = WebDriverWait(self._driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, HomePageLocators.TOP_SEARCH_RESULT.value))
            )
            return top_search_result.text
        except Exception as e:
            self.logger.error("Failed to get the top search result: %s", str(e))
            raise

    def click_save_to_library_button(self):
        """Click the save to library button."""
        try:
            save_to_library_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.SAVE_TO_LIBRARY_BUTTON.value))
            )
            save_to_library_button.click()
        except Exception as e:
            self.logger.error("Failed to click the save to library button: %s", str(e))
            raise

    def click_more_options_button(self):
        """Click the more options button."""
        try:
            more_options_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.MORE_OPTIONS_BUTTON.value))
            )
            more_options_button.click()
        except Exception as e:
            self.logger.error("Failed to click the more options button: %s", str(e))
            raise

    def click_result_play_button(self):
        """Click the play button for a search result."""
        try:
            result_play_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.RESULT_PLAY_BUTTON.value))
            )
            result_play_button.click()
            time.sleep(3)
        except Exception as e:
            self.logger.error("Failed to click the result play button: %s", str(e))
            raise

    def click_result_pause_button(self):
        """Click the pause button for a search result."""
        try:
            result_pause_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.RESULT_PAUSE_BUTTON.value))
            )
            result_pause_button.click()
            time.sleep(2)
        except Exception as e:
            self.logger.error("Failed to click the result pause button: %s", str(e))
            raise

    def hover_on_add_to_playlist_button(self):
        """Hover over the add to playlist button."""
        try:
            add_to_playlist_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.ADD_TO_PLAYLIST_BUTTON.value))
            )
            ActionChains(self._driver).move_to_element(add_to_playlist_button).perform()
        except Exception as e:
            self.logger.error("Failed to hover on add to playlist button: %s", str(e))
            raise

    def click_Add_to_playlist_button(self):
        """Click the add to playlist button."""
        try:
            add_to_playlist_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.ADD_TO_TEST_PLAYLIST_BUTTON.value))
            )
            add_to_playlist_button.click()
            time.sleep(5)
        except Exception as e:
            self.logger.error("Failed to click the add to playlist button: %s", str(e))
            raise

    # ------------------------------------------------------------------------------------
    def click_test_playlist_button(self):
        """Click the test playlist button."""
        try:
            test_playlist_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.TEST_PLAYLIST_BUTTON.value))
            )
            self._driver.execute_script("arguments[0].scrollIntoView(true);", test_playlist_button)
            test_playlist_button.click()
            time.sleep(5)
        except Exception as e:
            self.logger.error("Failed to click the test playlist button: %s", str(e))
            raise

    def get_playlist_items(self):
        """Get the items in a playlist."""
        try:
            playlist_items = WebDriverWait(self._driver, 10).until(
                ec.visibility_of_all_elements_located((By.XPATH, HomePageLocators.PLAYLIST_ITEMS.value))
            )
            return playlist_items
        except Exception as e:
            self.logger.error("Failed to get playlist items: %s", str(e))
            raise

    def get_last_track_from_playlist(self, playlist_items):
        """Get the last track from the playlist items."""
        try:
            last_track = playlist_items[-1]
            return last_track
        except Exception as e:
            self.logger.error("Failed to get the last track from playlist: %s", str(e))
            raise

    def click_playlist_item_options_button(self, item):
        """Click the options button for a playlist item."""
        try:
            item.click()
            playlist_item_options_button = WebDriverWait(item, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.PLAYLIST_ITEM_OPTIONS_BUTTON.value))
            )
            playlist_item_options_button.click()
        except Exception as e:
            self.logger.error("Failed to click playlist item options button: %s", str(e))
            raise

    def click_playlist_item_remove_button(self):
        """Click the remove button for a playlist item."""
        try:
            playlist_item_remove_button = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.PLAYLIST_ITEM_REMOVE_BUTTON.value))
            )
            playlist_item_remove_button.click()
            time.sleep(2)
        except Exception as e:
            self.logger.error("Failed to click playlist item remove button: %s", str(e))
            raise

    def move_progress_bar(self, offset):
        """Move the progress bar to a specific offset."""
        try:
            progress_bar = WebDriverWait(self._driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, HomePageLocators.PROGRESS_BAR.value))
            )
            progress_bar_width = progress_bar.size['width']
            center_x_offset = progress_bar_width / 2
            target_x_offset = (progress_bar_width * offset) - center_x_offset
            ActionChains(self._driver).move_to_element_with_offset(progress_bar, target_x_offset, 0).click().perform()
            time.sleep(2)
        except Exception as e:
            self.logger.error("Failed to move progress bar: %s", str(e))
            raise
