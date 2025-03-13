
import os

from dotenv import load_dotenv
from langchain_core.language_models.chat_models import ChatGenerationChunk
from langchain_core.messages import AIMessageChunk
from langchain_core.runnables.config import (ensure_config,
                                             get_callback_manager_for_config)
from ollama import AsyncClient

from agent.utils.state import State

# Load environment variables
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_SERVICE_ENDPOINT")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME")

client = AsyncClient(host=OLLAMA_HOST)


async def call_agent(state: State, config=None):
    """
    The chatbot function that processes messages and streams the response from Ollama's API.
    """
    config = ensure_config(config | {"tags": ["agent_llm"]})
    callback_manager = get_callback_manager_for_config(config)
    messages = state["messages"]
    llm_run_manager = callback_manager.on_chat_model_start({}, [messages])[0]

    # Prepare the message structure
    # Get the last message (HumanMessage object)
    last_user_message = state["messages"][-1]
    # Access the content of the HumanMessage object
    message_content = last_user_message.content

    message = [
        {'role': 'system', 'content': 'You are helpful agent.'},
        {'role': 'user', 'content': message_content}
    ]

    # Start streaming the response from the Ollama model
    async for part in await client.chat(model=OLLAMA_MODEL_NAME, messages=message, tools=[], stream=True):
        if 'message' in part:
            if 'content' in part['message']:
                role = part['message']['role']
                content = part['message']['content']
                # note: we're wrapping the response in ChatGenerationChunk so that we can stream this back using stream_mode="messages"
                chunk = ChatGenerationChunk(
                    message=AIMessageChunk(
                        content=content,
                    )
                )
                llm_run_manager.on_llm_new_token(content, chunk=chunk)

        response_message = {
            "role": role,
            "content": content
        }
        yield {"messages": [response_message]}
