## Shows a simple demonstration of agentops using openai API keys

import os
from dotenv import load_dotenv

load_dotenv()

# ###################################################
agentops_api_key = os.getenv("AGENTOPS_API_KEY1")
import agentops

agentops.init(agentops_api_key, tags=["app1"])
# ###################################################

openai_api_key = os.getenv("OPENAI_KEY")

from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {
            "role": "assistant",
            "content": "The Los Angeles Dodgers won the World Series in 2020.",
        },
        {"role": "user", "content": "Where was it played?"},
    ],
)

print(response.choices[0].message.content)

###################################
agentops.end_session("Success")
###################################
