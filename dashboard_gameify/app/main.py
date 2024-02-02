# main.py
from app.api_client import SnykAPIClient
from app.data_store import DataStore
from app.dashboard import Dashboard
from app.scheduler import start_scheduler

# Set your Snyk API key
SNYK_API_KEY = "your_snyk_api_key"

# Set your AWS DynamoDB table name
DYNAMODB_TABLE_NAME = "your_dynamodb_table_name"

# Define teams and repositories
TEAMS = ["team1", "team2"]
REPOSITORIES = ["repo1", "repo2"]

# Initialize API client, data store, and dashboard
api_client = SnykAPIClient(SNYK_API_KEY)
data_store = DataStore(DYNAMODB_TABLE_NAME)
dashboard = Dashboard(data_store)

# Start the scheduler
start_scheduler(api_client, data_store, TEAMS, REPOSITORIES)

# Run your dashboard functions as needed
dashboard.generate_trend_graph("team1", "repo1")
dashboard.generate_leaderboard()
