from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
result = model.invoke("What is the capital of Delhi")

print(result)
print(result.content)
