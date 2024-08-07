import pickle
import time

import requests
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


def jira_aio_upload(token, cycle_id):
    import requests

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
    files = {
        'file': ('report.xml', open(r'C:\Users\evoix\PycharmProjects\project-finale\report.xml', 'rb'))
    }
    data = {
        'updateDatasets': 'true',
        'createNewRun': 'true',
        'addCaseToCycle': 'true'
    }

    # Make the request
    response = requests.post(url, headers=headers, params=query, files=files, data=data)
    print(response.status_code, response.text)



