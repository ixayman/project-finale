import logging


class Logger:
    @staticmethod
    def setup_logger(name):
        logging.basicConfig(level=logging.INFO,  # Change this to INFO or higher
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("../test_log.log"),
                                logging.StreamHandler()
                            ])
        logger = logging.getLogger(name)
        # Set Selenium logging level to WARNING to filter out DEBUG messages
        logging.getLogger('selenium.webdriver.common.selenium_manager').setLevel(logging.WARNING)
        return logger
