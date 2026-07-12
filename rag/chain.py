import os
from dotenv import load_dotenv

if not os.getenv("GROQ_API_KEY"):
    load_dotenv()


from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from rag.prompt import prompt
from rag.retriever import Retriever


class RealEstateRAG:

    def __init__(self):

        

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY").strip()
)

        self.retriever = Retriever()

        self.parser = StrOutputParser()

    def ask(self, question):

        docs = self.retriever.retrieve(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        chain = (
            prompt
            | self.llm
            | self.parser
        )

        answer = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        sources = []

        for doc in docs:
            sources.append(doc.metadata.get("source"))

        return answer, list(set(sources))