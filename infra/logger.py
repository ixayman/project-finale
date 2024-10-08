import logging
import os


class Logger:
    @staticmethod
    def setup_logger(name):
        # Create a logger
        log_file_path = os.path.join(os.path.dirname(__file__), '../test_log.log')
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Create handlers
        file_handler = logging.FileHandler(log_file_path)  # Logs will be saved to test_log.log
        stream_handler = logging.StreamHandler()

        # Set level for handlers
        file_handler.setLevel(logging.INFO)
        stream_handler.setLevel(logging.INFO)

        # Create formatters and add them to handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger
