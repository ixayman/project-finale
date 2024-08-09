import json
import os


class SecretHandler:
    secret_path = os.path.join(os.path.dirname(__file__), '../client_secret.json')

    @staticmethod
    def load_from_file():
        """Load JSON data from the secret file."""
        try:
            with open(SecretHandler.secret_path, 'r') as f:
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
            with open(SecretHandler.secret_path, 'w') as f:
                json.dump(data, f, indent=4)
                print("Secret saved successfully!")
        except Exception as e:
            print(f"An error occurred while saving: {e}")
            exit(-1)
