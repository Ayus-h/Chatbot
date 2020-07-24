import requests
import spacy

def city_check(question):
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(question)

    for ent in doc.ents:
        if len(ent) > 0:
            city = str(ent)
            return city
        else:
            pass


def setting(city):
    add1 = "https://openweathermap.org/data/2.5/weather?q="
    add2 = "&appid=b6907d289e10d714a6e88b30761fae22"
    url = add1 + city + add2
    jsondata = requests.get(url).json()
    return jsondata

def weather(city):
    jsondata = setting(city)
    formatdata = jsondata['weather'][0]["main"]
    #print("Todays weather in {} is {}")
    return str(formatdata.lower())

def temp(city):
    jsondata = setting(city)
    tempdata = jsondata['main']
    temp = tempdata['temp']
    return temp

'''
if __name__=="__main__":
    question = str(input("Please type something.\n")).lower()
    city = city_check(question)
    try:
        print(weather(city))
        print(temp(city))
    except TypeError:
        print("No city.")
'''