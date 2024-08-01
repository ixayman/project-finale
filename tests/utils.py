import pickle


def load_cookies(driver):
    try:
        # Load cookies from file
        with open('../cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
    except Exception as e:
        return f"Error loading cookies: %s {e}"
    # Refresh the browser to apply cookies
    driver.refresh()
    return
