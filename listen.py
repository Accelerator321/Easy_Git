import speech_recognition as sr
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
        text = '\n'

        while(text== '\n'):
            text = input()
        return text
    text =None
    while(text ==None):
        text = takecom()
        if(text ==None): print("Could not listen")
        else:
            print(f"you said: {text}")
    return text
        

        
