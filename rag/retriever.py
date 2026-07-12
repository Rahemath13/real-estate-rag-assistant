"""
retriever.py

Loads the FAISS vector store and retrieves
the most relevant document chunks.
"""

from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        embedding = EmbeddingModel().get_embedding_model()

        vector_db = VectorStore(embedding).load_vector_store()

        self.retriever = vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

    def retrieve(self, query: str):

        return self.retriever.invoke(query)