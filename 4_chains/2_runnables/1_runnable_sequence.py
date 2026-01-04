from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)

# Method 1
# chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# Method 2 - Shorthand
chain = prompt1 | model | parser | prompt2 | model | parser

print(chain.invoke({"topic": "AI"}))
