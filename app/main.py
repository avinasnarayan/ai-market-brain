from fastapi import FastAPI
from app.routes.news import router as news_router
from app.routes.prediction import router as prediction_router
from app.workers.scheduler import start_scheduler
import threading

app = FastAPI()

# include routes
app.include_router(news_router)
app.include_router(prediction_router)

@app.get("/")
def root():
    return {"message": "AI Market Brain API running"}

# start scheduler when server starts
@app.on_event("startup")
def startup_event():
    print("Starting background news scheduler...")

    def run_scheduler():
        start_scheduler()

    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True
    thread.start()