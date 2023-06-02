#open AI
fileopen=open("data\\api.txt","r")
API=fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv
#import speak


#coding
openai.api_key=API
load_dotenv()
completion=openai.Completion()


def ReplyBrain(question,chat_log=None):
    File_log=open("data\\api.txt","r")
    chat_log_template=File_log.read()
    File_log.close()

    if chat_log is None:
        chat_log=chat_log_template
    
    prompt=f'{chat_log}you : {question}\nCharlie : '
    response = completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0)
    answer=response.choices[0].text.strip()
    chat_log_template_update=chat_log_template + f"\nYou : {question} \nCharlie : {answer}"
    File_log=open("","w")
    File_log.write(chat_log_template_update)
    File_log.close()
    return answer
ans=ReplyBrain("Hello Charlie How are you")

print(ans)
