from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a friendly AI assistant. Answer the question in a helpful and concise manner.")
]
model_name = "llama3.2:3b"

while True:
    user_input = input("You: ")
    user_role = HumanMessage(content=user_input)
    messages.append(user_role)

    if user_input.lower() in ["quit", "exit"]:
        break

    llm=ChatOllama(model=model_name)
    response = llm.invoke(messages)
    response = response.content
    print("Assistant: " + response)
