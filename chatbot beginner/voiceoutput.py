import pyttsx3 as pt

def speak(text):
    engine = pt.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)

    engine.say(text)

    engine.runAndWait()

