from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chat_history = []


system_message = SystemMessage(content="You are a helpful assistant.")
print(f"System message: {system_message}")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        exit()

    human_message = HumanMessage(content=query)
    chat_history.append(human_message)

    result = model.invoke(chat_history)

    if result.content:
        ai_message = AIMessage(result.content)
        print(f"AI message: {ai_message.content}")
        chat_history.append(ai_message)
    else:
        print("AI message: Sorry, I don't have an answer for that.")
