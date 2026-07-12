from rag.embeddings import EmbeddingModel

embedding = EmbeddingModel().get_embedding_model()

vector = embedding.embed_query(
    "Tell me about payment plans."
)

print(f"Vector Length : {len(vector)}")

print(vector[:10])