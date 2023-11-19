import os

from openai import OpenAI
from dotenv import load_dotenv
from threading import Timer

load_dotenv()
KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI()
client.api_key = KEY

default_message = 'You are a chat bot in a discord server. Your task will be to answer questions given to you by it\'s members. '
context = [default_message]

def clear_context():
    context.clear
    context.append(default_message)
    print('Context post-clear: ' + ' '.join(context))

timer = Timer(10 * 60, clear_context())

def ask_gpt(arg):
    if(timer.is_alive() == False):
        timer.start()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "Here's the context so far: " + ' '.join(context)},
            {"role": "user", "content": ' '.join(arg)}
        ]
    )
    response = completion.choices[0].message.content
    context.append(response + ' ')
    return response

def split_on_dot(string):
    split = string[:1900].rfind('.')
    return [string[:split], string[split:len(string)-1]]
