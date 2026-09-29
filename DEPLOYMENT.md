# DocuChat AI — Deployment & Cloud Setup Guide

This guide covers deployment instructions and explains the differences between local execution and cloud deployment.

---

## ⚡ Quick Start: Deploying to Streamlit Cloud with Groq (Llama 3.2)

### Step 1: Push Code to GitHub
```bash
git add .
git commit -m "Add Groq API support for Streamlit Cloud"
git push origin main
```

### Step 2: Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com) and sign in for free.
2. Click **API Keys** -> **Create API Key**.
3. Copy your API key (starts with `gsk_...`).

### Step 3: Configure Streamlit Cloud Secrets (Optional but Recommended)
1. In your Streamlit Cloud app dashboard, click **Settings** -> **Secrets**.
2. Add your key in TOML format:
   ```toml
   GROQ_API_KEY = "gsk_your_groq_api_key_here"
   ```
3. Save secrets. Your app will automatically use **Llama 3.2 via Groq Cloud API** for all users without requiring them to type an API key in the UI!

> Alternatively, users can enter their Groq API Key directly in the sidebar settings.

---

## 🔄 Changes Made when Moving from Local to Deployed

| Component | Local Machine | Cloud Deployment (Streamlit Cloud) | Reason for Change |
|---|---|---|---|
| **Primary LLM** | Ollama (`llama3.2` on `localhost:11434`) | **Groq Cloud API** (`llama-3.2-3b-preview`) | Streamlit Cloud containers don't run Ollama natively. |
| **Package Imports** | Standard `langchain` modules | `langchain-text-splitters` & `langchain-groq` | Newer LangChain package modularization requires explicit split sub-packages in `requirements.txt`. |
| **Embeddings** | Ollama (`nomic-embed-text`) | `sentence-transformers` (`all-MiniLM-L6-v2`) | Fallback to PyTorch/HuggingFace embeddings when local Ollama is offline. |
| **Database & Cache** | Stored on local disk | Dynamically initialized per container instance | Added `.gitignore` to prevent committing test user accounts (`users.db`) or local vector files. |

---

## 📦 Docker Deployment (Alternative Self-Hosted Cloud)

If you prefer self-hosting Ollama and DocuChat together in Docker:

```yaml
version: '3.8'
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_storage:/root/.ollama

  docuchat:
    build: .
    ports:
      - "8501:8501"
    environment:
      - OLLAMA_HOST=http://ollama:11434
    volumes:
      - ./users.db:/app/users.db
      - ./vector_cache:/app/vector_cache
    depends_on:
      - ollama

volumes:
  ollama_storage:
```

Run with:
```bash
docker-compose up -d --build
```
