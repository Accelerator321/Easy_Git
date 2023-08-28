import speech_recognition as sr
from speak import wreak
def takecom():
    r = sr.Recognizer()
    try:
            
        with sr.Microphone() as source:
            # r.pause_threshold = 1
            r.energy_threshold = 3000
            print("Listening........")
            audio = r.listen(source,timeout=5)
            query = r.recognize_google(audio, language="en-in")
            return query

    except Exception:
        return None

def listen(read= True):
    if(read):
        text = None

        while(not text):
            print("you:", end=" ")
            text = input()
        return text
    text =None
    while(text ==None):
        text = takecom()
        if(text ==None): wreak("Could not listen")
        else:
            print(f"you: {text}")
    return text
        

        
