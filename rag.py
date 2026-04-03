from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load embeddings + vector DB
embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# Load LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def ask_question(query):
    result = qa_chain.invoke({"query": query})
    return result["result"], result["source_documents"]