from phi.agent import Agent
from phi.model.groq import Groq
from load_knowledge_base import knowledge_base
from phi.tools.duckduckgo import DuckDuckGo
# from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv 
from phi.model.vertexai import Gemini
from phi.tools.googlesearch import GoogleSearch


load_dotenv()

healthcare_agent = Agent(
    name="Health-Care Agent",
    model=Groq(id="gemma2-9b-it"),
    instructions=[
    "Your only goal is to assists the user with healthcare and health insurace related queries.",
    "Use knowledge base to answer the query but if you aren't able to get a definitive answer then use google search to answer"   
],
    knowledge=knowledge_base,
    search_knowledge=True,
    tools=[GoogleSearch()], # websearch for knowledge gap
    # Add a tool to read chat history.
    read_chat_history=True,
    add_datetime_to_instructions=True,
    # show_tool_calls=True,
    markdown = True,
)

# healthcare_agent.knowledge.load(recreate=False)
