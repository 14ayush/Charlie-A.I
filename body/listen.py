import speech_recognition as sr
from googletrans import Translator
# listining :hindi and english
def listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source,0,9)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="hi")
    except:
        return ""
    query=str(query).lower()
    return query


# Translator
def TranslationHinToEng(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"you: {data}.")
    return data


# Connect

def mic():
    query=listen()
    data=TranslationHinToEng(query)
    return data 
mic()