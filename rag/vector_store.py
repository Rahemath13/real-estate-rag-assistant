"""
vector_store.py

Creates and loads the FAISS vector database.
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.index_path = Path("data/vector_store")

    def create_vector_store(self, chunks):

        print("\nCreating FAISS Vector Store...\n")

        vector_db = FAISS.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
        )

        self.index_path.mkdir(parents=True, exist_ok=True)

        vector_db.save_local(str(self.index_path))

        print("\nVector Store Saved Successfully.\n")

        return vector_db

    def load_vector_store(self):

        if not self.index_path.exists():
            raise FileNotFoundError(
                "Vector Store not found. Run ingest.py first."
            )

        vector_db = FAISS.load_local(
            str(self.index_path),
            self.embedding_model,
            allow_dangerous_deserialization=True,
        )

        return vector_db