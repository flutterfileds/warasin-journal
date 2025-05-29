import joblib

model = joblib.load("app/models/linear_svc_model.pkl")
vectorizer = joblib.load("app/models/tfidf_vectorizer.pkl")
encoder = joblib.load("app/models/label_encoder.pkl")