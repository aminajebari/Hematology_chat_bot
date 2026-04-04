# 🩸 Hematology AI Assistant

An AI-powered assistant designed to answer questions about hematology diseases using a **Retrieval-Augmented Generation (RAG)** architecture.
This project runs **fully locally**, without requiring paid APIs.

---

## 🚀 Features

* 💬 Answer general hematology questions (anemia, leukemia, lymphoma, etc.)
* 🧠 Explain diseases (symptoms, causes, diagnosis, treatment)
* 🔍 Retrieve relevant medical knowledge from custom datasets (CSV, TXT)
* 📄 Support structured medical data ingestion
* 🤖 Use local embeddings and vector database for semantic search
* 🔐 Fully local setup (no OpenAI API key required)

---

## 🏗️ Architecture

This project follows a **RAG pipeline**:

```
User Question
     ↓
Embedding (HuggingFace)
     ↓
Vector Database (Chroma)
     ↓
Retriever (top-k relevant chunks)
     ↓
LLM (Ollama - local model)
     ↓
Generated Answer
```

---

## 🧩 How It Works

1. **Data Ingestion (`ingest.py`)**

   * Loads medical data from CSV/TXT files
   * Splits text into smaller chunks
   * Converts text into embeddings
   * Stores embeddings in a vector database (Chroma)

2. **Vector Database (`vector_db/`)**

   * Stores text + embeddings
   * Enables fast semantic search

3. **Query System (`query.py`)**

   * Converts user question into embeddings
   * Retrieves most relevant chunks
   * Sends them to a local LLM
   * Generates a contextual answer

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **ChromaDB** (vector database)
* **HuggingFace Embeddings**
* **Ollama** (local LLM: phi / tinyllama / etc.)

---

## 📂 Project Structure

```
hematology-ai/
│
├── data/              # Medical datasets (CSV, TXT)
├── vector_db/         # Vector database (auto-generated)
├── ingest.py          # Data ingestion pipeline
├── query.py           # Question-answering system
└── README.md          # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/hematology-ai.git
cd hematology-ai
```

---

### 2. Create environment

```
conda create -n hematology-ai python=3.10
conda activate hematology-ai
```

---

### 3. Install dependencies

```
pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers
```

---

### 4. Install Ollama

Download and install:

👉 https://ollama.com/download

---

### 5. Run a lightweight model

```
ollama run phi
```

---

## ▶️ Usage

### Step 1 — Ingest data

```
python ingest.py
```

This will:

* Process your dataset
* Create the `vector_db/`

---

### Step 2 — Ask questions

```
python query.py
```

Example queries:

```
What is anemia?
What are the symptoms of leukemia?
Difference between lymphoma and leukemia?
```

---

## 🧪 Example

**Input:**

```
What is anemia?
```

**Output:**

```
Anemia is a medical condition characterized by a انخفاض in hemoglobin levels...
```

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
It does **not provide medical diagnosis or professional healthcare advice**.

---

## 🚀 Future Improvements

* 💬 Streamlit chatbot UI
* 📚 Support for PDF medical books
* 📊 Add citations (source documents)
* 🧠 Improve medical prompting
* 🔍 Hybrid search (semantic + keyword)
* 🧾 Structured outputs (Symptoms / Causes / Treatment)

---

## 👩‍💻 Author

**Amina Jebari**
Engineering Student – AI & Data

---

## ⭐ Contributing

Contributions are welcome!
Feel free to fork the project and submit a pull request.

---

## 📌 Key Concept

> This project does NOT train a model.
> It uses **Retrieval-Augmented Generation (RAG)** to combine:
>
> * Search (vector database)
> * Understanding (embeddings)
> * Generation (LLM)

---
