"""
embeddings.py

Creates the embedding model used by the RAG pipeline.
"""

from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Loads the Hugging Face embedding model.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5"
    ):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def get_embedding_model(self):
        return self.embedding_model