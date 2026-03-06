from fastapi import FastAPI
from app.routes.news import router as news_router
from app.workers.scheduler import start_scheduler
import threading

app = FastAPI()


@app.on_event("startup")
def startup_event():

    thread = threading.Thread(target=start_scheduler)
    thread.daemon = True
    thread.start()


app.include_router(news_router)