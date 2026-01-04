from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# -------------v1 - simple
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI: ", result.content)


# -------------v2 - chat history input
chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)
