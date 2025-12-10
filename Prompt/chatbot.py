from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv()

model = ChatOpenAI()
chat_history = [
    SystemMessage(content="Hello World"),
]
while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "quit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(chat_history)
