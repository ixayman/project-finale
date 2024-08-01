import json
from infra.config_provider import ConfigProvider


class SecretHandler:
    config = ConfigProvider.load_from_file()

    @staticmethod
    def load_from_file():
        """Load JSON data from the secret file."""
        try:
            with open(SecretHandler.config['client_secret_file'], 'r') as f:
                secret = json.load(f)
                return secret
        except FileNotFoundError:
            print("File client_secret.json not found.")
            exit(-1)
        except json.JSONDecodeError:
            print("Error decoding JSON from file client_secret.json.")
            exit(-1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit(-1)

    @staticmethod
    def save_to_file(data):
        """Save data to the secret file."""
        try:
            with open(SecretHandler.config['client_secret_file'], 'w') as f:
                json.dump(data, f, indent=4)
                print("Secret saved successfully!")
        except Exception as e:
            print(f"An error occurred while saving: {e}")
            exit(-1)
