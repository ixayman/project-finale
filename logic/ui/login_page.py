import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from infra.ui.base_page import BasePage


class LoginPage(BasePage):
    # Define XPATH locators for elements on the page
    USERNAME_INPUT = '//input[@id="login-username"]'
    PASSWORD_INPUT = '//input[@id="login-password"]'
    LOGIN_BUTTON = '//button[@id="login-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        # Initialize the elements
        self.username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
        self.password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self.login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def insert_username(self, username):
        self.username_input.send_keys(username)

    def insert_password(self, password):
        self.password_input.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def login_flow(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_login_button()
        WebDriverWait(self._driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//figure')))
