print("INGEST STARTED")

from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
docs = []

csv_loader = CSVLoader("data/hematology_qa.csv")
docs.extend(csv_loader.load())

txt_loader = TextLoader("data/hematology_notes.txt")
docs.extend(txt_loader.load())

print("Documents loaded:", len(docs))

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

print("Chunks:", len(chunks))



db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="vector_db"
)

db.persist()

print("Vector DB created successfully.")