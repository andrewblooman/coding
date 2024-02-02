# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def fetch_and_store_data(api_client, data_store, teams, repositories):
    for team in teams:
        for repo in repositories:
            vulnerabilities = api_client.get_vulnerabilities(team, repo)
            data_store.store_data(team, repo, vulnerabilities)
    print(f"Data fetched and stored at {datetime.now()}")

def start_scheduler(api_client, data_store, teams, repositories, interval_minutes=60):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        fetch_and_store_data,
        trigger="interval",
        minutes=interval_minutes,
        args=[api_client, data_store, teams, repositories],
    )
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
