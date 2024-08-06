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

    def drag_and_drop_playlist_item(self, index, destination_index):
        playlist_items = WebDriverWait(self._driver, 10).until(
            ec.visibility_of_all_elements_located((By.XPATH, HomePageLocators.PLAYLIST_ITEMS.value))
        )
        ActionChains(self._driver).drag_and_drop(playlist_items[index], playlist_items[destination_index]).perform()
