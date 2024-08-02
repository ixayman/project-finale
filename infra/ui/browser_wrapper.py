from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait

from infra.logger import Logger


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.logger = Logger.setup_logger(__name__)
        print("Test Start")

    def get_driver(self, config, page):
        try:
            browser = config.get("browser", "Firefox")  # Default to Firefox if not specified
            self.logger.info(f"Browser selected: {browser}")
            if browser == "Chrome":
                self._driver = webdriver.Chrome()
            elif browser == "Firefox":
                self._driver = webdriver.Firefox()
            else:
                raise ValueError(f"Unsupported browser: {browser}")

            url = config.get(page)
            if url:
                self._driver.maximize_window()
                self.logger.info(f"Navigating to URL: {url}")
                self._driver.get(url)
                WebDriverWait(self._driver, 10)
            else:
                self.logger.error(f"Page '{page}' not found in the configuration.")
                exit(-1)
            return self._driver
        except WebDriverException as e:
            self.logger.error(f"WebDriverException: {e}")
            raise

    def close_driver(self):
        self.logger = Logger.setup_logger(__name__)
        if self._driver:
            self._driver.close()
            self.logger.info("browser closed")
            self.logger.info("-" * 26)
            self._driver = None
        else:
            self.logger.warning("No driver to close")
