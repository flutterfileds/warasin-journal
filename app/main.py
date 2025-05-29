from fastapi import FastAPI
from pydantic import BaseModel
from app.model.predict import predict_emotion
from app.model.load_model import model, vectorizer, encoder

app = FastAPI()

class JournalEntry(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to  warasin journal API!"}\
    
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(entry: JournalEntry):
    emotion = predict_emotion(entry.text, model, vectorizer, encoder)
    return {"mood": emotion}

