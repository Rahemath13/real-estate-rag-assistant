"""
ingest.py

Runs the complete ingestion pipeline.
"""

from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


def main():

    print("=" * 60)
    print("REAL ESTATE RAG INGESTION")
    print("=" * 60)

    loader = PDFLoader()
    documents = loader.load_documents()

    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)

    embedding_model = EmbeddingModel().get_embedding_model()

    vector_store = VectorStore(embedding_model)

    vector_store.create_vector_store(chunks)

    print("\nIngestion Completed Successfully")


if __name__ == "__main__":
    main()