# pyrefly: ignore [missing-import]
from fastapi import FastAPI

from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever

documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

retriever = HybridRetriever(documents)

app = FastAPI(
    title="AI Knowledge Base Assistant",
    version="1.0.0"
)

from utils.answer_generator import generate_answer
from utils.schema import (
    QuestionRequest,
    AnswerResponse
)


@app.post(
    "/ask",
    response_model=AnswerResponse
)
def ask_question(request: QuestionRequest):

    docs = retriever.search(
        request.question
    )

    response = generate_answer(
        request.question,
        docs
    )

    return response