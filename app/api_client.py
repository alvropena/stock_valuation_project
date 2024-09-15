import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class APIClient:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = "https://api.financialdatasets.ai"

    def make_request(self, endpoint, params=None):
        """Generic method to make requests to any financial dataset API endpoint."""
        headers = {
            "X-API-KEY": self.api_key
        }
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from {endpoint}: {response.status_code} - {response.text}")
