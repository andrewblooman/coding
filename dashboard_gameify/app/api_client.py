# api_client.py
import requests

class SnykAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.snyk.io/v1/"

    def get_vulnerabilities(self, team, repository):
        url = f"{self.base_url}org/{team}/project/{repository}/vuln/npm"
        headers = {"Authorization": f"token {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json()
