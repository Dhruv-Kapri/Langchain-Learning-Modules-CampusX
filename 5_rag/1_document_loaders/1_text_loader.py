from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
project_root = Path(__file__).parents[2]
curr_path = project_root / "5_rag" / "1_document_loaders"
doc_path = curr_path / "documents"

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()

loader = TextLoader(file_path=doc_path / "cricket.txt")
doc = loader.load()

# print(type(doc))
# print(type(doc[0]))
# print(doc[0])
# print(doc[0].page_content)
# print(doc[0].metadata)

prompt = PromptTemplate(
    template="Write a summary of the poem. \n Poem: {text}", input_variables=["text"]
)

chain = prompt | model | parser
result = chain.invoke({"text": doc[0].page_content})

print(result)
