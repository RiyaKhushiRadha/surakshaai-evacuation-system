from fastapi import FastAPI

app = FastAPI(title="SuRakshaAI Backend")

@app.get("/")
def read_root():
    return {"message": "SuRakshaAI backend is running!"}