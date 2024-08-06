import json


class ConfigProvider:

    @staticmethod
    def load_from_file():
        try:
            with open(r'C:\Users\evoix\PycharmProjects\5tech\project-finale\config.json', 'r') as f:
                config = json.load(f)
                return config
        except FileNotFoundError:
            print(f"File config.json not found.")
            exit(-1)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file config.json.")
            exit(-1)
