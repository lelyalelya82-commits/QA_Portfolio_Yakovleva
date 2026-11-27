import os
import requests
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

load_dotenv(dotenv_path=env_path)


class YougileApi:
    def __init__(self):
        self.base_url = os.getenv("YOUGILE_BASE_URL")
        self.token = os.getenv("YOUGILE_TOKEN")

        if not self.token:
            raise ValueError(
                "Токен не найден! Проверьте, что файл .env "
                f"лежит по пути: {env_path}"
            )

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload):
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers
        )

    def update_project(self, project_id, payload):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
