import os

import requests


class APIClient:
    def __init__(self):
        self.session = requests.Session()

    def base_url(self):
        return os.getenv("BASE_URL", "https://poetrydb.org/")

    def get(self, api_path):
        full_url = f"{self.base_url()}{api_path}"
        return self.session.get(full_url)
