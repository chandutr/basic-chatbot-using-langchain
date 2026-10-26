from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI assistant. Answer questions helpfully and concisely."),
    ("user", "{question}")
])

llm = ChatOllama(model="llama3.2:3b")

parser = StrOutputParser()

chain = prompt_template | llm | parser

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("AI: Goodbye!")
        break

    messages.append(("user", user_input))

    response = chain.invoke({"question": user_input})
    messages.append(("assistant", response))

    print("AI:", response)