from pathlib import Path

from langchain_community.document_loaders import CSVLoader

project_root = Path(__file__).parents[2]
curr_path = project_root / "5_rag" / "1_document_loaders"
doc_path = curr_path / "documents"


loader = CSVLoader(file_path=doc_path / "Social_Network_Ads.csv")
doc = loader.load()

print(type(doc))
print(type(doc[0]))
# print(doc[0])                      # single row of the table
print(doc[5].page_content)
print(doc[5].metadata)
