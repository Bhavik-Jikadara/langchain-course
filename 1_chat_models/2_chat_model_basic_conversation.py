from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# SystemMessage: Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse: Message from a human to the AI model.
# AIMessage: Message from an AI.
messages = [
    SystemMessage(content="Answer the user questions based on the provided context."),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Ask from User: {messages[1].content}")
print(f"Answer from AI: {result.content}")