from fastapi import FastAPI
from rag import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hematology AI Assistant Running"}

@app.get("/ask")
def ask(q: str):
    answer, sources = ask_question(q)

    return {
        "question": q,
        "answer": answer,
        "sources": [str(doc) for doc in sources]
    }