from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox actio and yorkers.",
]

querry = "tell me about bumrah"

doc_embeddings = embedding.embed_documents(documents)
querry_embedding = embedding.embed_query(querry)

scores = cosine_similarity([querry_embedding], doc_embeddings)[0]
scores = list(enumerate(scores))
scores = sorted(scores, key=lambda x: x[1])

index, score = scores[-1]

print(querry)
print(documents[index])
print("similarity score is:", float(score))
