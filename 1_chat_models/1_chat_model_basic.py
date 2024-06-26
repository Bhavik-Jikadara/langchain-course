from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model=os.getenv("OPENAI_MODEL_NAME"))

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)