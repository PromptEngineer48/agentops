## Shows how to record agents

import os
from dotenv import load_dotenv

load_dotenv()

###################################################
agentops_api_key = os.getenv("AGENTOPS_API_KEY1")
import agentops

agentops.init(agentops_api_key, tags=["app4"])
###################################################

openai_api_key = os.getenv("OPENAI_KEY")
from openai import OpenAI

client = OpenAI(api_key=openai_api_key)


@agentops.track_agent("QaAgent")
class QaAgent:
    @agentops.record_function("QaAgent_Completion Run")
    def completion(self, prompt: str):
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a qa engineer and only output python code, no markdown tags.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        return res.choices[0].message.content


@agentops.track_agent("EngineerAgent")
class EngineerAgent:
    @agentops.record_function("EngineerAgent_Completion Run")
    def completion(self, prompt: str):
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a software engineer and only output python code, no markdown tags.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        return res.choices[0].message.content


qa = QaAgent()
engineer = EngineerAgent()

generated_func = engineer.completion(
    "Write a python function that accepts two numbers and multiplies them together, then divides by two. No example."
)

print("```python\n" + generated_func + "\n```")


generated_test = qa.completion(
    "Write a python unit test that test the following function: \n " + generated_func
)

print("```python\n" + generated_test + "\n```")


###################################
agentops.end_session("Success")
###################################
