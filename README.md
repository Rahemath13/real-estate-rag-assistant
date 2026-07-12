# 🏠 Real Estate AI Assistant (RAG)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-purple)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-blueviolet)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-black)

---

# 📌 Project Overview

Real Estate AI Assistant is a Retrieval-Augmented Generation (RAG) application that answers real-estate related questions using project brochures, payment plans, RERA summaries and builder documents.

Instead of generating answers from general knowledge, the assistant retrieves the most relevant information from the provided knowledge base and uses a Large Language Model (Groq Llama 3.3 70B) to generate accurate, grounded responses with source citations.

This project demonstrates a production-oriented RAG architecture using LangChain, FAISS, HuggingFace Embeddings, FastAPI and Streamlit.

---

# ✨ Features

- Secure Login Authentication
- Retrieval Augmented Generation (RAG)
- PDF Knowledge Base
- Automatic PDF Parsing
- Text Chunking
- HuggingFace Embeddings
- FAISS Vector Database
- Semantic Search
- Groq Llama 3.3 70B Integration
- Source Document Citation
- Streamlit Chat Interface
- FastAPI Backend
- Modular Project Structure
- Docker Support
- GitHub Actions CI Pipeline
- Production Ready Architecture

---

# 🏗 System Architecture

```

                +---------------------+
                |   Streamlit UI      |
                +----------+----------+
|
User Question
|
v
+---------------------+
| FastAPI Backend |
+----------+----------+
|
v
+---------------------+
| LangChain RAG |
+----------+----------+
|
+-----------+------------+
| |
v v
FAISS Vector DB Groq LLM
|
v
PDF Knowledge Base

```

---

# 🛠 Technology Stack

### Programming

- Python 3.11

### Frontend

- Streamlit

### Backend

- FastAPI
- Uvicorn

### AI / LLM

- LangChain
- Groq
- HuggingFace Embeddings

### Vector Database

- FAISS

### Document Processing

- PyPDF
- Recursive Character Text Splitter

### DevOps

- Docker
- GitHub Actions
- GitHub

---

# 📁 Project Structure

```

real_estate_rag_assistance/

├── .github/
│ └── workflows/
│ └── deploy.yml
│
├── app/
│ ├── components/
│ │ ├── sidebar.py
│ │ ├── footer.py
│ │ ├── source_panel.py
│ │ └── chat_message.py
│ │
│ └── pages/
│ ├── login.py
│ └── chat.py
│
├── backend/
│ ├── api.py
│ └── auth.py
│
├── config/
│ └── settings.py
│
├── data/
│ ├── raw/
│ └── vector_store/
│
├── rag/
│ ├── loader.py
│ ├── splitter.py
│ ├── embeddings.py
│ ├── vector_store.py
│ ├── retriever.py
│ ├── chain.py
│ └── ingest.py
│
├── tests/
│
├── utils/
│ └── logger.py
│
├── Dockerfile
├── requirements.txt
├── main.py
├── README.md
└── .env

```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository_url>

cd real_estate_rag_assistance
```

Install dependencies

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 📚 Build Knowledge Base

Generate the FAISS Vector Store.

```bash
python -m rag.ingest
```

---

# ▶️ Run Streamlit Application

```bash
streamlit run main.py
```

Open

```

http://localhost:8501

```

---

# ⚡ Run FastAPI Backend

```bash
uv run uvicorn backend.api:app --reload
```

Swagger UI

```

http://127.0.0.1:8000/docs

```

---

# 💬 Sample Questions

- What is the payment plan of Urban Nest?
- Compare HBP and Meridian projects.
- Tell me about Skyline Builder.
- Is the project RERA approved?
- What amenities are available?
- Who is the builder?

---

# 🐳 Docker

Build

```bash
docker build -t real-estate-rag .
```

Run

```bash
docker run -p 8501:8501 real-estate-rag
```

---

# ☁ GitHub

```bash
git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin <repository>

git push -u origin main
```

---

# 🔄 GitHub Actions (CI)

Pipeline performs

- Checkout Repository
- Install Dependencies
- Validate Python Code
- Build Docker Image

Workflow

```

Developer

↓

Git Push

↓

GitHub Repository

↓

GitHub Actions

↓

Install Dependencies

↓

Run Validation

↓

Build Docker Image

↓

Ready for Deployment

```

---

# 🚀 Deployment

Recommended Platform

- Render

Deployment Steps

1. Connect GitHub Repository
2. Configure Environment Variables
3. Automatic Build
4. Automatic Deployment
5. Public URL Generation

Every push to the `main` branch automatically triggers the CI pipeline.

---

# 📊 RAG Workflow

```

User Question

↓

Embedding Generation

↓

FAISS Similarity Search

↓

Top Relevant Chunks

↓

Groq LLM

↓

Grounded Response

↓

Source Documents

```

---

# 🧪 Testing

Test the following:

- Login Authentication
- Chat Interface
- PDF Retrieval
- Source Citation
- FastAPI Endpoints
- Vector Database Loading

---

# 🔒 Security

- Environment variables managed using `.env`
- API keys are never hardcoded
- Modular backend architecture
- Authentication layer separated from business logic

---

# 🚀 Future Enhancements

- JWT Authentication
- Conversation Memory
- Chat History Database
- User Management
- Multi-Agent Workflow
- Hybrid Search
- OCR Support
- Image Search
- Admin Dashboard
- Cloud Vector Database
- Monitoring & Logging

---

# 👨‍💻 Author

**Mohammad Rahemath**

AI / Machine Learning Engineer

Generative AI • RAG • LangChain • FastAPI • Streamlit • FAISS • Groq

---

# 📄 License

This project was developed as part of a technical assessment for educational and evaluation purposes.
