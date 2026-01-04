from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

messages = [
    SystemMessage(content="You are a helpful all-knowing assistant"),
    HumanMessage(content="Tell me about Langchain"),
]

result = model.invoke(messages)

messages.append(SystemMessage(content=result.content))

print(messages)
