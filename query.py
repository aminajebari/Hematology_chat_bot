from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

retriever = db.as_retriever()

# Use local LLM (Ollama)
llm = Ollama(model="llama3")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

while True:
    query = input("Ask a hematology question: ")
    result = qa.run(query)
    print("\nAnswer:\n", result)