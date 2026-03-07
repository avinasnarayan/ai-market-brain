from fastapi import FastAPI
from app.routes.news import router as news_router
from app.workers.scheduler import start_scheduler

app = FastAPI()

# include routes
app.include_router(news_router)

@app.get("/")
def root():
    return {"message": "AI Market Brain API running"}

# start background scheduler
start_scheduler()