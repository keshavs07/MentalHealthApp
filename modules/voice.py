import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand"