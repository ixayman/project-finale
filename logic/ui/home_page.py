import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from logic.entity.ui_locators import HomePageLocators
from infra.ui.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize the elements

    def click_cookie_close_button(self):
        cookie_close_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.COOKIE_CLOSE_BUTTON.value))
        )
        cookie_close_button.click()

    def click_login_button(self):
        login_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.LOGIN_BUTTON.value))
        )
        login_button.click()
        WebDriverWait(self._driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                                '//h1[text()="Log in to Spotify"]')))

    def click_signup_button(self):
        signup_button = WebDriverWait(self._driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, HomePageLocators.SIGNUP_BUTTON.value))
        )
        signup_button.click()

    def click_playlist_from_library(self, playlist_name):
        library_list = WebDriverWait(self._driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, HomePageLocators.LIBRARY_LIST.value))
        )
        playlist = WebDriverWait(library_list, 10).until(
            ec.element_to_be_clickable((By.XPATH, f'//span[text()="{playlist_name}"]'))
        )
        ActionChains(self._driver).move_to_element(playlist).perform()
        playlist.click()

    def click_search_button(self):
        search_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.SEARCH_BUTTON.value))
        )
        search_button.click()

    def insert_in_search_field(self, text):
        search_field = WebDriverWait(self._driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, HomePageLocators.SEARCH_FIELD.value))
        )
        search_field.send_keys(text)

    def click_top_search_result(self):
        top_search_result = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.TOP_SEARCH_RESULT.value))
        )
        top_search_result.click()

    def click_save_to_library_button(self):
        save_to_library_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.SAVE_TO_LIBRARY_BUTTON.value))
        )
        save_to_library_button.click()

    def click_more_options_button(self):
        more_options_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.MORE_OPTIONS_BUTTON.value))
        )
        more_options_button.click()


    def click_result_play_button(self):
        result_play_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.RESULT_PLAY_BUTTON.value))
        )
        result_play_button.click()
        time.sleep(2)

    def click_result_pause_button(self):
        result_pause_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.RESULT_PAUSE_BUTTON.value))
        )
        result_pause_button.click()
        time.sleep(2)

    def hover_on_add_to_playlist_button(self):
        add_to_playlist_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.ADD_TO_PLAYLIST_BUTTON.value))
        )
        ActionChains(self._driver).move_to_element(add_to_playlist_button).perform()

    def click_test_playlist_button(self):
        test_playlist_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.TEST_PLAYLIST_BUTTON.value))
        )
        test_playlist_button.click()
        time.sleep(5)

    def drag_and_drop_playlist_item(self, index, destination_index):
        playlist_items = WebDriverWait(self._driver, 10).until(
            ec.visibility_of_all_elements_located((By.XPATH, HomePageLocators.PLAYLIST_ITEMS.value))
        )
        ActionChains(self._driver).drag_and_drop(playlist_items[index], playlist_items[destination_index]).perform()

    def move_progress_bar(self, offset):
        progress_bar = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.PROGRESS_BAR.value))
        )
        progress_bar_width = progress_bar.size['width']
        center_x_offset = progress_bar_width / 2
        target_x_offset = (progress_bar_width * offset) - center_x_offset
        ActionChains(self._driver).move_to_element_with_offset(progress_bar, target_x_offset, 0).click().perform()
        time.sleep(2)
