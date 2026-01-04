from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n text: {text}",
    input_variables=["text"],
)


# Method 1 -> Manual sequential
prompt1 = template1.invoke({"topice": "black hole"})
result = model.invoke(prompt1)
prompt2 = template2.invoke({"text": result.content})
result = model.invoke(prompt2)
print(result.content)

# Method 2 -> chaining
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"text": "black hole"})
print(result)
