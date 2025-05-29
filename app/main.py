import os
import nltk
import re
import string
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.predict import predict_emotion
from app.model.load_model import model, vectorizer, encoder

nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")

if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)
    print(f"Created NLTK data directory: {nltk_data_dir}")

nltk.data.path.append(nltk_data_dir)
print(f"Added {nltk_data_dir} to NLTK data paths.")

corpora_to_download = ['punkt', 'wordnet', 'punkt_tab']

for corpus in corpora_to_download:
    try:
        # NLTK uses different internal paths for tokenizers vs. corpora
        if corpus in ['punkt', 'punkt_tab']: # 'punkt' and 'punkt_tab' are tokenizers
            nltk.data.find(f'tokenizers/{corpus}')
        else: # 'wordnet' is a corpus
            nltk.data.find(f'corpora/{corpus}')
        print(f"NLTK '{corpus}' corpus already downloaded.")
    except nltk.downloader.DownloadError:
        print(f"NLTK '{corpus}' corpus not found, downloading...")
        nltk.download(corpus, download_dir=nltk_data_dir)
        print(f"NLTK '{corpus}' corpus downloaded successfully.")
    except LookupError: # Fallback for cases where find might not catch it
        print(f"NLTK '{corpus}' corpus not found (LookupError), downloading...")
        nltk.download(corpus, download_dir=nltk_data_dir)
        print(f"NLTK '{corpus}' corpus downloaded successfully.")

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

