from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

project_root = Path(__file__).parents[2]
curr_path = project_root / "5_rag" / "1_document_loaders"
doc_path = curr_path / "documents"


loader = PyPDFLoader(file_path=doc_path / "dl-curriculum.pdf")
doc = loader.load()

print(type(doc))
print(type(doc[0]))
# print(doc[0])
print(doc[0].page_content)
print(doc[0].metadata)
