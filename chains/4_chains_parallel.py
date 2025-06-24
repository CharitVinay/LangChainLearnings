from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain.schema.output_parser import StrOutputParser

# Create a ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}."),
    ]
)

# Define pros analysis step
def analyze_pros(features):                                                     
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the pros of these features.",
            ),
        ]
    )
    return pros_template.format_prompt(features=features)

# Define cons analysis step
def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the cons of these features.",
            ),
        ]
    )
    return cons_template.format_prompt(features=features)

def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"

# Simplify branches with LCEL
pros_chain_branch = (
    RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser()
)
cons_chain_branch = (
    RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
)

# Combine branches in parallel
chain = ( 
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(
        {
            "pros": pros_chain_branch,
            "cons": cons_chain_branch,
        }
    )
    | RunnableLambda(lambda x: combine_pros_cons(x["pros"], x["cons"]))
)

# Run the chain
result = chain.invoke({"product_name": "iPhone 15 Pro"})

# Output
print(result)

