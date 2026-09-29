"""
DocuChat AI — Step-by-Step Pipeline Demonstration Script

This standalone script demonstrates the exact step-by-step RAG pipeline
executed by DocuChat AI behind the scenes:
  Step 1: Document Text Ingestion
  Step 2: Recursive Character Text Chunking
  Step 3: Embedding Generation & FAISS Indexing
  Step 4: Similarity Search Retrieval
  Step 5: RAG Prompt Construction & LLM Response Generation
"""

import sys
import io

# Ensure UTF-8 output formatting for Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def run_pipeline_demo():
    print("=" * 60)
    print("DOCUCHAT AI -- STEP-BY-STEP WORKFLOW DEMONSTRATION")
    print("=" * 60)

    # -------------------------------------------------------------------------
    # STEP 1: Text Ingestion (Simulated multi-document input)
    # -------------------------------------------------------------------------
    print("\n[STEP 1] Text Ingestion & Parsing")
    sample_text = """
    DocuChat AI is a local document intelligence system built with Python, Streamlit, 
    FAISS, and LangChain. It enables users to upload PDF, DOCX, PPTX, XLSX, and TXT files.
    All document processing and vector embeddings stay 100% local on the user's machine.
    
    The user database uses SQLite for secure authentication. 
    Text extraction uses ThreadPoolExecutor for parallel file parsing.
    Similarity searches query top-k relevant document chunks to construct context for LLMs.
    """
    print(f"Extracted Text Length: {len(sample_text)} characters")
    print(f"Sample snippet:\n{sample_text.strip()[:150]}...")

    # -------------------------------------------------------------------------
    # STEP 2: Text Chunking
    # -------------------------------------------------------------------------
    print("\n[STEP 2] Recursive Character Text Chunking")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=30,
        length_function=len
    )
    chunks = text_splitter.split_text(sample_text)
    print(f"Generated {len(chunks)} text chunks with overlap of 30 chars.")
    for i, chunk in enumerate(chunks, 1):
        print(f"  Chunk [{i}]: {chunk.strip()}")

    # -------------------------------------------------------------------------
    # STEP 3: Vector Embeddings & Index Building
    # -------------------------------------------------------------------------
    print("\n[STEP 3] Generating Embeddings & FAISS Vector Indexing")
    print("Loading HuggingFace Embedding Model ('all-MiniLM-L6-v2')...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    print(f"FAISS Vector Store successfully indexed {len(chunks)} vectors.")

    # -------------------------------------------------------------------------
    # STEP 4: Similarity Search Retrieval
    # -------------------------------------------------------------------------
    user_query = "How does DocuChat handle file parsing and privacy?"
    print(f"\n[STEP 4] Similarity Search for Query: '{user_query}'")
    
    retrieved_docs = vectorstore.similarity_search(user_query, k=2)
    print(f"Retrieved Top {len(retrieved_docs)} matching chunks:")
    for idx, doc in enumerate(retrieved_docs, 1):
        print(f"  Result {idx}: {doc.page_content.strip()}")

    # -------------------------------------------------------------------------
    # STEP 5: Prompt Construction
    # -------------------------------------------------------------------------
    print("\n[STEP 5] RAG Prompt Construction")
    context_str = "\n".join([d.page_content.strip() for d in retrieved_docs])
    prompt = (
        "Answer the user query in a natural, friendly, conversational way based strictly on the context below.\n\n"
        f"Context:\n{context_str}\n\n"
        f"Question: {user_query}\n\n"
        "Answer:"
    )
    print("Constructed LLM Prompt:")
    print("-" * 40)
    print(prompt)
    print("-" * 40)

    print("\nPIPELINE DEMO COMPLETE: The constructed prompt is sent to Ollama/HF for generation!")

if __name__ == "__main__":
    run_pipeline_demo()
