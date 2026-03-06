from pydantic import BaseModel

class NewsOut(BaseModel):
    title: str
    source: str
    sentiment: str
    impact_score: float
    sector: str

    class Config:
        orm_mode = True