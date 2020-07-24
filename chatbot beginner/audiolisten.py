import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

        try:
            text = r.recognize(audio)
            print("You said {}".format(text))
            return text
        except:
            print("Did not understand that.")






