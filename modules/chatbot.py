import requests

def chatbot_response(text):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"You are a helpful mental health assistant. User: {text}"
            }
        )
        return response.json().get("response", "I'm here for you.")
    except:
        return "Chatbot not available."