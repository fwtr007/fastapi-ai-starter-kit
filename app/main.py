from fastapi import FastAPI

app = FastAPI(title="FastAPI AI Starter Kit")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI AI Starter Kit API"}
