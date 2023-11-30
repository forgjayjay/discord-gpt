import os
from tracemalloc import start

from openai import OpenAI
from dotenv import load_dotenv
from threading import Timer

load_dotenv()
KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI()
client.api_key = KEY

default_message = 'You are a chat bot in a discord server. Your task will be to answer questions given to you by it\'s members. '
channel_to_context = {}

timed_channels = []

def clear_context(id):
    channel_to_context.pop(id)

def ask_gpt(arg, id):
    # if id not in timed_channels:
    #     start_timer(id)

    if id not in channel_to_context:
        channel_to_context[id] = [default_message]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "Here's the context so far: " + ' '.join(channel_to_context[id])},
            {"role": "user", "content": ' '.join(arg)}
        ]
    )
    response = completion.choices[0].message.content
    channel_to_context[id].append(response + ' ')
    return response

def start_timer(id, args = []):
    args.append(id)
    timer = Timer(10 * 60, clear_context, args=args[0])
    timed_channels.append(id)
    timer.start()
    timer.join()

def split_on_dot(string):
    split = string[:1900].rfind('.')
    return [string[:split], string[split:len(string)-1]]
