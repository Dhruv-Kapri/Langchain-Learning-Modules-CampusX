from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(
    model_name="claude-3-5-sonnet-20241022",
    timeout=30,
    stop=["\n\nHuman:"],
)
result = model.invoke("What is the capital of Delhi")

print(result)
print(result.content)
