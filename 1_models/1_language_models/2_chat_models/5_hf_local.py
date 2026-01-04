from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()
# token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
    ),
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Delhi?")
print(result.content)
