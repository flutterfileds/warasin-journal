import re
import string

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'(\w)\1{2,}', r'\1', text)

    tokens = text.split()

    return " ".join(tokens)