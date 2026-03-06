from fastapi import FastAPI
from app.routes.news import router as news_router
from app.workers.scheduler import start_scheduler
import threading

app = FastAPI(title="AI Market News Engine")

app.include_router(news_router)

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_scheduler)
    thread.daemon = True
    thread.start()