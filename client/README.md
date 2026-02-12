# 🧠 DocuMind - Frontend (Streamlit)

This is the sleek, interactive Streamlit frontend for DocuMind. It provides a premium interface for document intelligence, allowing users to upload PDFs, engage in RAG-powered conversations, and analyze retrieval quality.

---

## Features

- 📄 **Multi-PDF Intelligence**: Upload and chat with multiple documents simultaneously.
- 🧠 **Smart Model Switching**: Choose between different LLM backends on the fly.
- 🔬 **Deep Dive Inspector**: Analyze direct vectorstore queries to understand the RAG process.
- 📥 **Export Insights**: Download your chat history as a structured CSV.

---

## Project Structure

```
client/
├── app.py                      # Main Streamlit entry point
├── state/
│   └── session.py              # Handles session state setup
├── components/
│   ├── chat.py                 # All chat-related UI components
│   ├── sidebar.py              # Configuration and utilities
│   └── inspector.py            # RAG transparency tools
├── utils/
│   ├── api.py                  # Backend bridge
│   ├── config.py               # Constants and endpoints
│   └── helpers.py              # UI logic and orchestration
```

---

## 📦 Installation

```bash
cd client
pip3 install -r requirements.txt
```

---

## ▶️ Usage

1. Start the [Backend Server](../server).
2. Run the client:

```bash
streamlit run app.py
```

### Steps to Success:
1. **Configure**: Select a model provider and model.
2. **Upload**: Drag and drop your PDFs.
3. **Submit**: Click **Submit** to index the documents.
4. **Chat**: Engage with your documents in the chat interface!

---

## Configuration

Set `API_URL` in `client/utils/config.py`:
```python
API_URL = "http://localhost:8000"
```

---

## 🛠️ Utilities

- **🔄 Reset**: Full session reset.
- **🧹 Clear Chat**: Wipe conversation and document context.
- **↩️ Undo**: Remove the last interaction.

---

## ⚠️ Requirements

- Backend (FastAPI) must be running.
- Valid API keys (Groq or Gemini) must be configured in the backend environment.
