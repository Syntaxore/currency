import requests
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Settings:
    api_key: str = None

    def __post_init__(self):
        self.api_key = os.getenv("API_KEY")

class Currency(Settings):
    def __init__(self):
        super().__init__()

    def _get(self, url):
        res = requests.get(url)
        res.raise_for_status()
        return res

    def get_pair(self, value1: str, value2: str, amount: float):
        try:
            res = self._get(
                f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{value1}/{value2}/{amount}"
            )
            data = res.json()
            if data.get("result") != "success":
                return {"error": data.get("error-type", "unknown")}
            return data
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP {e.response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}