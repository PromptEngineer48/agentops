## created a new function and recorded the function using decorators

import os
from dotenv import load_dotenv

load_dotenv()

###################################################
agentops_api_key = os.getenv("AGENTOPS_API_KEY1")
import agentops


agentops.init(agentops_api_key, tags=["app2"])


###################################################

openai_api_key = os.getenv("OPENAI_KEY")

from openai import OpenAI

client = OpenAI(api_key=openai_api_key)


@agentops.record_function("responder function activate")
def responder():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
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

    return response


response = responder()
print(response.choices[0].message.content)

response = responder()
print(response.choices[0].message.content)

###################################
agentops.end_session("Success")
###################################
