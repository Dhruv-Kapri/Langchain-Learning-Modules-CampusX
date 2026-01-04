from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

project_root = Path(__file__).parents[2]
curr_path = project_root / "5_rag" / "1_document_loaders"
doc_path = curr_path / "documents"


loader = DirectoryLoader(
    path=str(doc_path) + "/books", glob="*.pdf", loader_cls=PyPDFLoader
)
docs = loader.lazy_load()

print(type(docs))

for document in docs:
    print(type(document))
    # print(document)
    print(document.page_content)
    print(document.metadata)
    # break
