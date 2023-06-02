import pyttsx3

def speak(Text):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',180)
    print("")
    print(f"You: {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

speak("Hello Sir . I am Jarvis. How I can help you sir..... ")


