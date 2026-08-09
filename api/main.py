# pyrefly: ignore [missing-import]

# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException
from utils.query_rewriter import rewrite_query
from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever
from utils.answer_generator import generate_answer
from utils.logger import logger
from utils.schema import QuestionRequest, AnswerResponse


# --------------------------------------------------
# Load Knowledge Base
# --------------------------------------------------

logger.info("Loading company documents...")

documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

logger.info(
    f"Loaded {len(documents)} document chunks."
)

retriever = HybridRetriever(documents)

logger.info("Hybrid Retriever initialized.")


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="AI Knowledge Base Assistant",
    version="1.0.0"
)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Knowledge Base Assistant API is running."
    }


# --------------------------------------------------
# Ask Endpoint
# --------------------------------------------------

@app.post(
    "/ask",
    response_model=AnswerResponse
)
def ask_question(request: QuestionRequest):

    try:

        # Validate question
        if not request.question.strip():

            logger.warning(
                "Empty question received."
            )

            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty."
            )

        logger.info(
            f"Received Question: {request.question}"
        )

        original_question = request.question

        transformed_question = rewrite_query(
            original_question
        )

        logger.info(
            f"Transformed query: {transformed_question}"
        )

        docs = retriever.search(
            transformed_question
        )

        logger.info(
            f"Retrieved {len(docs)} documents."
        )

        # Handle no results
        if not docs:

            logger.warning(
                "No relevant documents found."
            )

            raise HTTPException(
                status_code=404,
                detail=(
                    "No relevant information found "
                    "in the knowledge base."
                )
            )

        # Generate answer
        response = generate_answer(
            original_question,
            docs
        )

        logger.info(
            "Response generated successfully."
        )

        return response

    except HTTPException:
        raise

    except Exception as e:

        logger.error(
            f"Unexpected error while processing request: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to process your request."
        )