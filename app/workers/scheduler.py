from apscheduler.schedulers.background import BackgroundScheduler
from app.services.news_pipeline import run_news_pipeline
import time

def start_scheduler():

    scheduler = BackgroundScheduler()

    # run every 5 minutes
    scheduler.add_job(run_news_pipeline, "interval", minutes=5)

    scheduler.start()

    print("✅ News scheduler started (runs every 5 minutes)")

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()