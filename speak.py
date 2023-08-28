import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(speech):
    '''This fuction speaks the argument given to it.
    But you have to set the voice using
    engine.setProperty('voice', voices[0 or 1].id) first'''

    pyttsx3.speak(speech)
    engine.runAndWait()

def wreak(text):
    '''This function writes and speaks the given arguments.
    It uses speak function'''
    print(text)
    speak(text)