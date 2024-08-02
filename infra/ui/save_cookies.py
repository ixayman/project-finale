import pickle
import time

from infra.ui.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.secret_handler import SecretHandler
from logic.ui.login_page import LoginPage
from logic.ui.home_page import HomePage


def save_login_cookies():
    """
    run standalone to save login cookies
    """
    secret = SecretHandler.load_from_file()
    config = ConfigProvider.load_from_file()
    browser = BrowserWrapper()
    driver = browser.get_driver(config, "home_page")
    base_page = HomePage(driver)
    base_page.click_login_button()
    login_page = LoginPage(driver)
    login_page.login_flow(secret['username'], secret['password'])
    # Save cookies to file
    cookies = driver.get_cookies()
    with open(config['cookies_file'], 'wb') as file:
        pickle.dump(cookies, file)
    driver.quit()


save_login_cookies()
