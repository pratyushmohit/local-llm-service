from langgraph.graph import END, START, StateGraph

from agent.utils.nodes import call_model
from agent.utils.state import State

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", call_model)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()


async def stream_agent_updates(user_input: str):
    inputs = {"messages": [{"role": "user", "content": user_input}]}
    async for message, _ in graph.astream(inputs, stream_mode="messages"):
        if message.content:
            yield {
                "role": "assistant",
                "content": message.content
            }
