# crewai : working

import os

from crewai import Agent, Task, Crew, Process

# from langchain.llms import Ollama
# ollama_openhermes = Ollama(model="openhermes")

import os

os.environ["OPENAI_API_KEY"] = "<YOUR API KEY">

import agentops

agentops.init("<AGENTOPS API KEY>", tags=["app5-crewai-gpt4"])


researcher = Agent(
    role="Researcher",
    goal="Discover new insights",
    verbose=True,
    backstory=(
        "You are a world class researcher working on a major data science company"
    ),
    allow_delegation=False,
)

writer = Agent(
    role="Writer",
    goal="Create Engaging content",
    verbose=True,
    backstory=(
        "You are a famous technical writer, specialized on writing data related content"
    ),
    allow_delegation=False,
)

task1 = Task(
    description=("Investigate the latest AI trends"),
    expected_output="Investigate the latest AI trends",
    agent=researcher,
)
tast2 = Task(
    description=("Write a blog post on AI advancements"),
    expected_output="Write a detailed blog post",
    agent=writer,
)


crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, tast2],
    verbose=True,
)


result = crew.kickoff()


print("The outputs have been compiled")
print("Result=> ", result)

agentops.end_session("Success")
