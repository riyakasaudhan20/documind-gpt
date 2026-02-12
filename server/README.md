# 🤖 DocuMind - Backend (FastAPI)

This is the robust FastAPI backend for DocuMind. It orchestrates PDF parsing, vector embedding using ChromaDB, and intelligent retrieval-augmented generation (RAG) using LangChain.

---

## Features

- ✅ **Asynchronous PDF Processing**: Handles multiple uploads efficiently.
- 🧠 **Multi-Provider Support**: Seamlessly switch between Groq and Gemini.
- 🔍 **Vector Transparency**: Inspect similarity search results and chunks.
- 🛡️ **Pydantic Validation**: Strong typing for all API inputs and outputs.

---

## Project Structure

```
server/
├── api/                        # FastAPI routes and schemas
├── config/                     # Environment and constants
├── core/                       # LLM logic, vectorstore, processing
├── utils/                      # Logger and helpers
├── main.py                     # App entry point
```

---

## 📦 Installation

```bash
cd server
pip3 install -r requirements.txt
```

---

## Configuration

Set your API keys in a `.env` file in this directory:

- **Groq**: [console.groq.com](https://console.groq.com/)
- **Gemini**: [ai.google.dev](https://ai.google.dev)

```env
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_key
```

---

## ▶️ Usage

Run the server:

```bash
uvicorn main:app --reload
```

---

## API Endpoints

- `POST /upload_and_process_pdfs`: Process documents for a provider.
- `POST /chat`: Start a RAG session.
- `GET /vector_store/count/{provider}`: Get indexed document count.
- `POST /vector_store/search`: Perform a test similarity search.
- `GET /llm`: List available providers.
- `GET /llm/{provider}`: List models for a provider.
- `GET /health`: System status check.

