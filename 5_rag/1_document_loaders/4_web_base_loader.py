from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"
loader = WebBaseLoader(web_path=url)
doc = loader.load()

print(type(doc))
print(type(doc[0]))
# print(doc[0])
print(doc[0].page_content)
print(doc[0].metadata)
