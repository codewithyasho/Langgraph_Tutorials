"""
Stock Market Trading Agent with Human-in-the-Loop Decision Making
"""

from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.types import interrupt, Command
from typing import TypedDict, Annotated, List
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage

# memory for the agent
memory = MemorySaver()


# state initialization
class AgentState(TypedDict):
    messages: Annotated[List, add_messages]


# ----------------- Tools for the agent ----------------- #

# Tool 1 - get the current stock price for a given company
@tool
def get_stock_price(company: str) -> str:
    """
    Returns the current stock price for the given company.
    Args:
        company (str): The company name to look up.
    returns:
        The current stock price.
    """
    return {
        "Microsoft": 423.37,
        "Apple": 269.96,
        "Google": 344.90,
        "Amazon": 242.96,
        "Nvidia": 185.61,
        "Meta": 706.41,
    }.get(company.capitalize(), "Company not found")


# Tool 2 - buy stocks for a given company
@tool
def buy_stocks(company: str, quantity: int, total_price: float) -> str:
    """
    Buys a specified quantity of stocks for the given company.
    Args:
        company (str): The company name to buy stocks from.
        quantity (int): The number of stocks to buy.
        total_price (float): The total price of the stocks to buy.

    returns:
        Confirmation message of the purchase.
    """

    decision = interrupt(
        f"Do you want to buy {quantity} shares of {company} for ${total_price}? (yes/no)")

    if decision.lower() == "yes":
        return f"✅You bought {quantity} shares of {company} for ${total_price}."

    else:
        return "❌ Transaction cancelled."


# Tool 3 - sell stocks for a given company
@tool
def sell_stocks(company: str, quantity: int, total_price: float) -> str:
    """
    Sells a specified quantity of stocks for the given company.
    Args:
        company (str): The company name to sell stocks from.
        quantity (int): The number of stocks to sell.
        total_price (float): The total price of the stocks to sell.

    returns:
        Confirmation message of the sold stocks.
    """
    decision = interrupt(
        f"Do you want to sell {quantity} shares of {company} for ${total_price}? (yes/no)")

    if decision.lower() == "yes":
        return f"✅You sold {quantity} shares of {company} for ${total_price}."

    else:
        return "❌ Transaction cancelled."


# Toolkit of the agent
tools = [get_stock_price, buy_stocks, sell_stocks]


# llm initialization
llm = ChatOllama(model="deepseek-v3.1:671b-cloud",
                 temperature=0.3).bind_tools(tools=tools)


# ----------------- agent node ----------------- #

def agent(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(content="""
    You are a stock market trading agent. Your goal is to help users make informed decisions about buying and selling stocks.
    Answer the user queries using the available tools to get stock prices, buy stocks, and sell stocks.
    Be accurate and concise in your responses.
    """)

    response = llm.invoke([system_prompt] + state["messages"])

    return {"messages": [response]}


# ----------------- Graph Building ----------------- #

graph = StateGraph(AgentState)

graph.add_node("agent", agent)

tools = ToolNode(tools=tools)
graph.add_node("tools", tools)

graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", tools_condition)

graph.add_edge("tools", "agent")

app = graph.compile(checkpointer=memory)


# configuring threads for memory
config = {
    "configurable": {"thread_id": "thread_1"},
}


if __name__ == "__main__":
    # ----------------- Invoking the agent ----------------- #
    while True:

        # normal user query
        user_input = input("\nEnter your query: ")
        if "exit" in user_input.lower():
            break

        response1 = app.invoke({
            "messages": [{"role": "user", "content": user_input}]
        }, config=config)

        isinterrupt = response1.get("__interrupt__")

        # human in the loop decision
        if isinterrupt:
            print(f"\nAGENT: {response1['messages'][-1].content}")

            decision = input("\nDo you want to Proceed (yes/no): ")

            response2 = app.invoke(Command(resume=decision), config=config)

            print(f"\nAGENT: {response2['messages'][-1].content}")

        else:
            print(f"\nAGENT: {response1['messages'][-1].content}")

    print("\nSession ended.")
