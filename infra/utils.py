import random
import string
import re


def generate_random_string(length):
    """
          generates a random letters string for a given length
          """
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string


def generate_random_email():
    """
          generates a random email
          """
    random_email = ''.join(random.choice(string.ascii_lowercase) for _ in range(8)) + '@example.com'
    return random_email


def convert_numberK_to_number(s):
    """
      Converts a string with a 'K' (representing thousands) to an integer.
      2K -> 2000
      """
    try:
        if s.endswith('K'):
            return int(float(s[:-1]) * 1000)
        else:
            return int(s)
    except ValueError as e:
        print(f"Invalid input for numberK to number conversion: {e}")


def convert_ago_time(s):
    """
      convert time string to a numerical value:
      example: 20 minutes ago -> -20
                2 hours ago -> -120
      """
    time = re.findall(r'\d+', s)
    if "minute" in s:
        return -int(time[0])
    elif "hour" in s:
        return -int(time[0]) * 60
    elif "day" in s:
        return -int(time[0]) * 60 * 24
    elif "year" in s:
        return -int(time[0]) * 60 * 24 * 365


def check_if_array_in_descending_order(arr):
    """
    returns true if a list is in descending order.
    """
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


def wait_for_element(action, expected, time, retries):
    result = action
    while result != expected and retries > 0:
        result = action
        time.sleep(time)
        retries = retries - 1
    return result


def extract_temperature_unit(s):
    """
    extract temperature unit from a string
        """
    if 'F' in s:
        return 'Fahrenheit'
    elif 'C' in s:
        return 'Celsius'
    else:
        return 'Kelvin'


def get_month_name(number):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    return months[number]
