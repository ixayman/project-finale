import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from logic.ui.entity.locators import HomePageLocators
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

    def click_search_button(self):
        search_button = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, HomePageLocators.SEARCH_BUTTON.value))
        )
        search_button.click()
