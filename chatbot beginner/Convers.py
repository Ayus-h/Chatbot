import time
import re
import random
#import Weather
import audiolisten
import voiceoutput
import spacy

nlp = spacy.load('en_core_web_lg')

#empty dicitionary for samples
samples = {}

name="Ayush"
weather = "sunny"
temperature="5"
#temperature=Weather.temp("coventry")


KeyWord=\
    {
    "greet":["hi","hello","hey"],
    "thankyou":["thank","thnx"],
    "goodbye":["bye","farewell"],
    "name":["your name","you called","who are you","name?"],
    "weather":["weather","weather now","climate","weather today","sunny","cloudy","rain"],
    "temperature":["how cold?","temperature today","temperature","cold"]
    }

bot_response=\
    {
    "activate": ['voice ready','voice activated'],
    "default": ['tell me more! I am listening.','why do you think that? what is it that makes you feel that? what?','how long have you felt this way?hmm...',
                'I find that extremely interesting','are you sure?','oh lol!',],
    'goodbye': ['goodbye for now',"hmm bye","See you"],
    'greet': ['Hello you! :)',"heya! Nice to meet you.", "Hello. What can I do for you?",
              "hello. Its a pleasure."],
    'thankyou': ['you are very welcome', "no problem"],
    "name":["my name is {0}".format(name),"I am {0}".format(name),"It's me, {0}".format(name),
      "{0} and yours?".format(name),"Hello, my name is {0}. It is a pleasure to meet you. May I ask your name?".format(name),],
    "weather":["today, its {0}".format(weather), "weather of today is {0}".format(weather), "at present, it is {0}".format(weather),],
    "temperature":["temperature is {0} degree centrigrade".format(temperature),"it is {0} degree centigrade".format(temperature)]
    }

#to respond to the user_message
def respond(message):
    if message == "activate":
        message = audiolisten.speech_to_text()

    else:
        pass
    user_intent = intent_verify(message)
    # gives a readymade response in case of no sentences
    key="default"
    if "weather" in message or "temperature" in message:
        city = "coventry"
        weather = "sunny"
        temperature = "5"
        time.sleep(random.randint(1, 2))
        string = ["today, it is {} in {} and it is {} degree centigrade".format(weather, city, temperature),
                  "Now it is {} in {} with temperature of {}".format(weather, city, temperature)]
        return voiceoutput.speak(random.choice(string))
    if user_intent in bot_response:
        key = user_intent
    time.sleep(random.randint(1, 2))
    return voiceoutput.speak(random.choice(bot_response[key]))


# Iterate over the keywords dictionary
for user_intent, keys in KeyWord.items():
    # Create regular expressions and compile them into samples objects
    samples[user_intent] = re.compile("|".join(keys))



# A fun to find the user intention in the user text
def intent_verify(message):
    matched_intent = None
    for user_intent, sample in samples.items():
        # checks for repeating sample
        if sample.search(message):
            matched_intent = user_intent
    return matched_intent


if __name__ == "__main__":
    while True:
        message = input("USER :\n ")
        if "exit()" in message:
            break
        respond(message)



