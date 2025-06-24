import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser

# Create a ChatGoogleGenAI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages( 
    [
        ('system', "You are a comedian who tells jokes about {topic}."),
        ('human', "Tell me {joke_count} jokes.")
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(result)