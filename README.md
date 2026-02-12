# 🧠 DocuMind - V1 (FastAPI + Streamlit)

DocuMind is a **production-ready** RAG (Retrieval-Augmented Generation) application that allows you to chat with multiple PDF documents seamlessly. It features a modular architecture with a **FastAPI** backend for heavy lifting and a **Streamlit** frontend for a premium user experience.

---

<details>
  <summary> 🔗 Helpful Links </summary>

- 🧑‍💻 [DocuMind Backend](/server)
- 🧑‍💻 [DocuMind Frontend](/client)

</details>

---

## 🏗️ Architecture

![architecture](/assets/rag-bot-fastapi-architecture.png)

---

## 🚀 Features

- 📁 Upload multiple PDFs and chat with them
- 🔌 Choose from Groq or Gemini as LLM providers
- 🔎 Query inspector for vectorstore transparency
- 🧠 RAG with LangChain + ChromaDB
- 📦 Streamlit frontend, FastAPI backend
- 🧪 Token-based chunking for LLM precision
- 💬 Downloadable chat history
- 🧰 Tools for reset, undo, clear
- 🌐 Fully API-driven interaction

---

<details>
  <summary>🛠️ Tech Stack</summary>

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **LLMs**: Groq & Gemini via LangChain
- **Vector DB**: ChromaDB
- **Embeddings**: HuggingFace & Google GenAI
- **Chunking**: TokenTextSplitter
- **Parsing**: PyPDF
- **Orchestration**: LangChain Retrieval Chain

</details>

---

## 📦 Installation

```bash
git clone https://github.com/your-username/documind.git
cd documind
```

Setup Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install frontend:

```bash
cd client
pip3 install -r requirements.txt
```

Install backend:

```bash
cd ../server
pip3 install -r requirements.txt
```

---

## 🔐 API Keys Required

- **Groq API key** from [console.groq.com](https://console.groq.com/)
- **Google Gemini API key** from [ai.google.dev](https://ai.google.dev/)

Create a `.env` file in the `server` directory:

```env
GROQ_API_KEY=your-groq-key
GOOGLE_API_KEY=your-google-key
```

---

## ▶️ Run DocuMind

Start FastAPI backend:

```bash
# Terminal 1
cd server
uvicorn main:app --reload
```

Start Streamlit frontend:

```bash
# Terminal 2
cd client
streamlit run app.py
```

---

<details>
  <summary>📁 Project Structure</summary>

```bash
documind/
├── client/                         # Streamlit Frontend
│   ├── app.py                      # Main Streamlit entrypoint
│   ├── components/                 # UI modules
│   │   ├── chat.py
│   │   ├── inspector.py
│   │   └── sidebar.py
│   ├── state/
│   │   └── session.py              # Session state manager
│   ├── utils/
│   │   ├── api.py                  # Talks to backend
│   │   ├── config.py               # API_URL and config values
│   │   └── helpers.py              # API wrappers for frontend
│   ├── requirements.txt
│   └── README.md
...
```

</details>


---

<details>
  <summary> 👓 Different Views </summary>

| View | Description |
|------|-------------|
| 💬 Chat | Renders chat bubbles, input box, and chat history download |
| 🔬 Inspector | Renders inspector to test vectorstore responses |

![views](/assets/rag-bot-fastapi-clean-ui-ux.gif)

</details>

---

<details>
  <summary>🧼 Tools Panel</summary>

| Button | Function |
|----------|--------|
| 🔄 Reset | Clears session state and reruns app |
| 🧹 Clear Chat | Clears chat + PDF submission |
| ↩️ Undo | Removes last question/response |

</details>

---

<details>
  <summary>📦 Download Chat History</summary>

Chat history is saved in the session state and can be exported as a CSV with the following columns:

| Question | Answer | Model Provider | Model Name | PDF File | Timestamp |
|----------|--------|----------------|------------|---------------------|-----------|
| What is this PDF about? | This PDF explains... | Groq | llama3-70b-8192 | file1.pdf, file2.pdf | 2025-07-03 21:00:00 |

</details>

---

<details>
  <summary>🙏 Acknowledgements</summary>

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq](https://console.groq.com/)
- [Google Gemini](https://ai.google.dev/)
- [Chroma](https://docs.trychroma.com/)

</details>

---

## 🧠 Getting Started

Ready to explore? Drop your PDFs and start chatting with DocuMind!

---

Happy building! 🛠️
