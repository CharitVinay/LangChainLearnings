import os
from langchain_openai import ChatOpenAI
import logging

logger = logging.getLogger(__name__)

model = ChatOpenAI(model="gpt-4o")
print(f"Model initialized: {model}")
print(f"Calling model with a test prompt...")
result = model.invoke("What is the capital of India?")
print(f"Model response: {result}")
logger.info(f"Model response: {result}")
