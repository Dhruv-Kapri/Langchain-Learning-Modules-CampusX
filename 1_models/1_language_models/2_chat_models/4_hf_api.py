import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India")
# result = llm.invoke("What is the capital of India")

# print(result)
print(result.content)
print(result.content)
