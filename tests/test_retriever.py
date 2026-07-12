from rag.retriever import Retriever

retriever = Retriever()

docs = retriever.retrieve(
    "What are the payment plans?"
)

print("="*80)

for i, doc in enumerate(docs,1):

    print(f"\nResult {i}")

    print("-"*60)

    print(doc.page_content[:500])

    print("\nMetadata")

    print(doc.metadata)