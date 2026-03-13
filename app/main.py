from fastapi import FastAPI
from app.routes.news import router as news_router
from app.workers.scheduler import start_scheduler

app = FastAPI()

# include routes
app.include_router(news_router)

@app.get("/")
def root():
    return {"message": "AI Market Brain API running"}

# start scheduler when server starts
import threading

@app.on_event("startup")
def startup_event():
    print("Starting background news scheduler...")

    def run_scheduler():
        start_news_scheduler()

    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True
    thread.start()