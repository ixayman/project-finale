import json
import os


class ConfigProvider:

    @staticmethod
    def load_from_file():
        config_path = os.path.join(os.path.dirname(__file__), '../config.json')
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                return config
        except FileNotFoundError:
            print(f"File config.json not found.")
            exit(-1)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file config.json.")
            exit(-1)
