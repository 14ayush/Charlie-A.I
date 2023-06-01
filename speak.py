import pyttsx3

#def speak(Text):
    #engine=pyttsx3.init("sapi5")
    #voices=engine.getProperty('voices')
    #engine.setProperty('voices',voices[0].id)
   # engine.setProperty('rate',180)
    #print("")
    #print(f"You: {Text}.")
    #print("")
    #engine.say(Text)
    #engine.runAndWait()

#speak("hello sir")



#chrome based
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from time import sleep


edge_options=Options()
edge_options.add_argument('--log-level--3')
edge_options.headless=False

path="Database\msedgedriver.exe"
driver=webdriver.Chrome(path,options=edge_options)
driver.maximize_window()

website= r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
buttonselect=Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
buttonselect.select_by_value('British English /Brian ')


def speak(Text):
    lengthtext=len(str(Text))
    if lengthtext==0:
        pass
    else:
        print("")
        print(f"Charlie: {Text}.")
        print("")
        data=str(Text)
        xpathofsec='/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()
        if lengthtext>=30:
            sleep(4)
        elif lengthtext>=40:
            sleep(6)
        elif lengthtext>=55:
            sleep(8)
        elif lengthtext>=70:
            sleep(10)
        elif lengthtext>=100:
            sleep(13)
        elif lengthtext>=120:
            sleep(14)
        else:
            sleep(2)
speak("Hello sir i am Charlie How i can Help You ")
