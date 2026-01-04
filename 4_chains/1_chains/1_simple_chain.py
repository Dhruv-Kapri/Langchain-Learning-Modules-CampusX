from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write 5 lines on {topic}.",
    input_variables=[],
)

chain = prompt | model | parser
result = chain.invoke({"topic": "black hole"})
print(result)

chain.get_graph().print_ascii()
