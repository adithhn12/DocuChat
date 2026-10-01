# 🤖 DocuChat

A Retrieval-Augmented Generation (RAG) based document chatbot that allows users to upload and interact with multiple document formats using context-aware AI responses.

🔗 **Live Demo:** https://adith-docuchat.streamlit.app/

---

## ✨ Features

- 📄 Upload and process multiple document formats
- 💬 Ask questions about uploaded documents
- 🔎 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤗 Hugging Face embeddings
- ⚡ Groq-powered Llama 3.2 generation
- 📚 Context-aware responses based on retrieved document content
- 🌐 Streamlit web interface
- ☁️ Deployed using Streamlit Community Cloud

---

## 🔄 How It Works

```text
        User Uploads Documents
                  │
                  ▼
        Document Text Extraction
                  │
                  ▼
             Text Chunking
                  │
                  ▼
       Hugging Face Embeddings
                  │
                  ▼
          Vector Search Index
                  │
                  ▼
          User Question
                  │
                  ▼
       Relevant Context Retrieval
                  │
                  ▼
        Groq Llama 3.2 LLM
                  │
                  ▼
          Context-Aware Answer
```

---

## 🧠 RAG Pipeline

DocuChat uses Retrieval-Augmented Generation to improve responses by providing the language model with relevant information retrieved from the uploaded documents.

The process consists of:

1. **Document Processing**  
   Uploaded documents are converted into text.

2. **Chunking**  
   Large documents are divided into smaller sections for efficient retrieval.

3. **Embedding Generation**  
   Hugging Face embedding models convert document chunks into vector representations.

4. **Semantic Retrieval**  
   Relevant document chunks are retrieved based on the user's question.

5. **Context Generation**  
   Retrieved content is provided as context to the language model.

6. **Response Generation**  
   Groq-hosted Llama 3.2 generates the final answer using the retrieved context.

---

## 🛠️ Technology Stack

### AI / Machine Learning

- Retrieval-Augmented Generation (RAG)
- Hugging Face
- Llama 3.2
- Groq
- Semantic Search
- Vector Embeddings

### Backend

- Python
- LangChain
- Streamlit

### Deployment

- Streamlit Community Cloud

---

## 📁 Project Structure

```text
DocuChat/
│
├── static/
│   └── ...
│
├── .devcontainer/
│   └── ...
│
├── app.py
├── pipeline_demo.py
├── requirements.txt
├── HOW_IT_WORKS.md
├── DEPLOYMENT.md
├── .gitignore
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/adithhn12/DocuChat.git
cd DocuChat
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Groq API

Set your Groq API key as an environment variable or configure it through Streamlit secrets.

Do not commit API keys or other sensitive credentials to the repository.

### 4. Start the application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🌐 Live Demo

Try the deployed application:

**https://adith-docuchat.streamlit.app/**

---

## 📚 Documentation

Additional documentation is available in the repository:

- `HOW_IT_WORKS.md` — Detailed explanation of the DocuChat workflow
- `DEPLOYMENT.md` — Deployment and configuration information
- `pipeline_demo.py` — Standalone demonstration of the RAG pipeline

---

## 🎯 Project Objective

The goal of DocuChat is to provide an intuitive way to interact with information contained in documents through natural-language queries.

Instead of manually searching through large documents, users can upload their files and ask questions while the RAG pipeline retrieves relevant information to provide context-aware responses.

---

## 🔮 Future Improvements

- Support for additional document formats
- Improved retrieval accuracy
- Conversation memory
- Source citations for retrieved content
- Advanced document management
- Multi-user document workspaces
- Improved response evaluation

---

## 👨‍💻 Author

**Adith HN**

MCA Student | AI/ML | Software Development

GitHub: https://github.com/adithhn12
