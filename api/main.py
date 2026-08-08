# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException

from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever
from utils.logger import logger

logger.info("Loading company documents...")

documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

logger.info(f"Loaded {len(documents)} document chunks.")

retriever = HybridRetriever(documents)

logger.info("Hybrid Retriever initialized.")


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

    logger.info(
        f"Received Question: {request.question}"
    )

    docs = retriever.search(
        request.question
    )
    if not docs:
        logger.warning(
        "No relevant documents found."
    )

    raise HTTPException(
        status_code=404,
        detail="No relevant information found in the knowledge base."
    )

    logger.info(
        f"Retrieved {len(docs)} documents."
    )

    response = generate_answer(
        request.question,
        docs
    )

    logger.info("Response generated successfully.")

    return response