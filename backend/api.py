from fastapi import FastAPI
from pydantic import BaseModel

from backend.auth import AuthService
from rag.chain import RealEstateRAG

app = FastAPI(
    title="Real Estate RAG API",
    version="1.0.0"
)

rag = RealEstateRAG()


class LoginRequest(BaseModel):
    username: str
    password: str


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Real Estate RAG API Running"
    }


@app.post("/login")
def login(data: LoginRequest):
    return AuthService.login(
        data.username,
        data.password
    )


@app.post("/chat")
def chat(data: ChatRequest):

    answer, sources = rag.ask(data.question)

    return {
        "answer": answer,
        "sources": sources
    }