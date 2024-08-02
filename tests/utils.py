import pickle
import time

from selenium.webdriver.support.wait import WebDriverWait


def load_cookies(driver, config):
    try:
        # Load cookies from file
        with open(config['cookies_file'], 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
    except Exception as e:
        return f"Error loading cookies: %s {e}"
    # Refresh the browser to apply cookies
    driver.refresh()
    time.sleep(5)
    return
