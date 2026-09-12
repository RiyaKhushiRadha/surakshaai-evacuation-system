from fastapi import FastAPI
from app.db.database import init_db

app = FastAPI(title="SuRakshaAI Backend")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "SuRakshaAI backend is running!"}