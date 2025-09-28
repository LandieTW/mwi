import os
import json

api_keys_path = os.path.join(os.path.dirname(__file__), '../api_keys.json')
try:
    with open(api_keys_path, 'r', encoding='utf-8') as file:
        keys = json.load(file)
        my_api_key = keys['my_api_key']
        my_secret_key = keys['my_secret_key']
except FileNotFoundError:
    raise FileNotFoundError(f"API keys file not found at {api_keys_path}. \
                            Please create the file with your API keys.")
