from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

project_root = Path(__file__).parents[2]
curr_path = project_root / "5_rag" / "2_text_splitters"

loader = PyPDFLoader(file_path=curr_path / "dl-curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0, separator=" ")

result = splitter.split_documents(docs)

print(type(result))
print(result[1].page_content)
print(result[1].metadata)
