from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="./sentiment_model"
)

def predict_sentiment(text):
    return classifier(text)[0]["label"]