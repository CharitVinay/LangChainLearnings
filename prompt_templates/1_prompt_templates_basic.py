from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# 1. create a prompt template using template string
template = "Tell me a joke about {topic}."
promptTemplate = ChatPromptTemplate.from_template(template)

prompt = promptTemplate.invoke({"topic": "software engineers"})
print(f"-----Prompt from Template-----\n{prompt}\n")


# 2. prompt with multiple placeholders
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}.            
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
print(f"\n----- Prompt with Multiple Placeholders -----\n{prompt}\n")

# 3. prompt with system and human messages (using tuples)
template_messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})      
print(f"\n----- Prompt with System and Human Messages (Tuple) -----\n{prompt}\n")

# 4. prompt with system and human messages (using message objects) this will not work if we need to append dynamically to the prompt then we need to follow the about procedure in tuple.
messages = [
    SystemMessage(content="You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me {joke_count} jokes."),
]       
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})  
print(f"\n----- Prompt with System and Human Messages (Message Objects) -----\n{prompt}\n")
