"""
loader.py

Loads every PDF present inside data/raw
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def __init__(self, data_path: str = "data/raw"):
        self.data_path = Path(data_path)

    def load_documents(self):

        documents = []

        pdf_files = list(self.data_path.glob("*.pdf"))

        if len(pdf_files) == 0:
            raise FileNotFoundError(
                "No PDF files found inside data/raw"
            )

        print(f"\nFound {len(pdf_files)} PDF files\n")

        for pdf in pdf_files:

            print(f"Loading : {pdf.name}")

            loader = PyPDFLoader(str(pdf))

            documents.extend(loader.load())

        print(f"\nTotal Pages Loaded : {len(documents)}\n")

        return documents


if __name__ == "__main__":

    loader = PDFLoader()

    docs = loader.load_documents()

    print(docs[0].page_content[:500])