from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that seacjes over the internet
    Args:
        query (str): The search query
    Returns:
        str: The search result
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]})
    print(f"Agent result: {result}")


if __name__ == "__main__":
    main()
