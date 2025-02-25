from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import os
import openai

import os
from dotenv import load_dotenv
openai.api_key = os.environ.get("OPENAI_API_KEY")

load_dotenv()

os.environ['GROQ_API_KEY'] = os.environ.get("GROQ_API_KEY")
os.environ['PHI_API_KEY'] = os.environ.get("PHI_API_KEY")
print(f"Api keys loaded successfully {os.environ.get('GROQ_API_KEY')} {os.environ.get('PHI_API_KEY')}")
print(f"OpenAI API key loaded successfully {os.getenv('OPENAI_API_KEY')}")


## Web Search Agent

web_search_agent = Agent(
    name = "Web Search Agent",
    role="Search the web for information",
    model = Groq(id="llama-3.2-11b-vision-preview"),
    tools = [DuckDuckGoTools()],
    instructions =["Always include the source of the information in the report"],
    show_tool_calls = True,
    markdown = True,
)

## Financial Agent

finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama-3.2-11b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent],
    instructions = ["Always include the source of the information in the report",
                   "Use tables to display data where possible."],
    show_tool_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA.", stream =True)

print(multi_ai_agent.print_response)
