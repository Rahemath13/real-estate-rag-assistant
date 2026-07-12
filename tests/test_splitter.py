from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter

loader = PDFLoader()
documents = loader.load_documents()

splitter = DocumentSplitter()

chunks = splitter.split_documents(documents)

print(f"\nTotal Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:\n")
print(chunks[0].metadata)