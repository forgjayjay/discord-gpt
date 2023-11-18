import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI()
client.api_key = KEY

def ask_gpt(arg):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a chat bot in a discord server. Your task will be to answer questions given to you by it's members."},
            {"role": "user", "content": arg}
        ]
    )
    response = completion.choices[0].message.content
    return response