from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input('You: ')
    if user_input.lower() == "exit":
        print("See you later!")
        break

    chat_history.append(HumanMessage(content=user_input))

    # Build prompt from message history
    prompt = "\n".join([msg.content for msg in chat_history])
    result = llm.invoke(prompt)

    response = result.content.strip()
    chat_history.append(AIMessage(content=response))

    print("AI:", response)
