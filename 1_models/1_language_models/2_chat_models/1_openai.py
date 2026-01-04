from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Temperature is a seed for same qs, same ans, similarity
model = ChatOpenAI(model="gpt-4", temperature=0.3, max_completion_tokens=10)
result = model.invoke("What is the capital of Delhi")

print(result)
print(result.content)
