import pickle
import time
import os
from infra.logger import Logger


def load_cookies(driver, config):
    logger = Logger.setup_logger(__name__)
    logger.info("Loading cookies")
    try:
        # Load cookies from file
        cookies_path = os.path.join(os.path.dirname(__file__), "../cookies.pkl")
        with open(cookies_path, 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
    except Exception as e:
        return f"Error loading cookies: %s {e}"
    # Refresh the browser to apply cookies
    driver.refresh()
    logger.info("Cookies loaded")
    time.sleep(5)
    return


def jira_aio_upload(token, cycle_id):
    import requests
    import os
    try:
        # API endpoint
        url = f'https://tcms.aiojiraapps.com/aio-tcms/api/v1/project/KAN/testcycle/{cycle_id}/import/results'

        # Your API credentials and headers
        headers = {
            'Authorization': 'AioAuth ' + token,
            'accept': 'application/json;charset=utf-8'
        }
        query = {
            'type': 'JUnit'
        }

        report_path = os.path.join(os.path.dirname(__file__), '../report.xml')
        # Open the file in a context manager to ensure it's properly closed
        with open(report_path, 'rb') as file:
            files = {
                'file': ('report.xml', file)
            }
            data = {
                'updateDatasets': 'true',
                'createNewRun': 'true',
                'addCaseToCycle': 'true'
            }

            # Make the request
            response = requests.post(url, headers=headers, params=query, files=files, data=data)

            # Raise an HTTPError if the response code is not successful
            response.raise_for_status()

            # Return the JSON response
            return response.json()

    except Exception as err:
        print(f"An error occurred: {err}")
