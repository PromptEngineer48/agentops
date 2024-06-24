## Shows how to manually craft an event

import os
from dotenv import load_dotenv

load_dotenv()

###################################################
agentops_api_key = os.getenv("AGENTOPS_API_KEY1")
import agentops

agentops.init(agentops_api_key, tags=["app3"])
###################################################

openai_api_key = os.getenv("OPENAI_KEY")
from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

from agentops import ActionEvent

message = ({"role": "user", "content": "Hello"},)
response = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=message, temperature=0.5
)

if "hello" in str(response.choices[0].message.content).lower():
    agentops.record(
        ActionEvent(
            action_type="Agent says hello",
            params=str(message),
            returns=str(response.choices[0].message.content),
        )
    )

print(response.choices[0].message.content)


###################################
agentops.end_session("Success")
###################################
