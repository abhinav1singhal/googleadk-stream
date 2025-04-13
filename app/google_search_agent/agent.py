from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent=Agent(
    #unique name of agent
    name="first_searc_agent",
    #LLM I want to use, make sure you check the name if llm
    model="gemini-2.0-flash", # Google AI Studio
    #short descrition of models purpose
    description="Google search using this agent",
    #instructions to set Agent's behaviour
    instruction="you are a researcher, you always stick to the facts.",
    #Add the tools for this agent. In this case we will use google_search as tool. This is a prebuult tool
    #you can create your our tool as well to act as a subagent
    tools=[google_search]
)