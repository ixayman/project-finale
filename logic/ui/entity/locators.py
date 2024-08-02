from enum import Enum


class HomePageLocators(Enum):
    LOGIN_BUTTON = '//button[@data-testid="login-button"]'
    SIGNUP_BUTTON = '//button[@data-testid="signup-button"]'
    SEARCH_BUTTON = '//a[@aria-label="Search"]'
