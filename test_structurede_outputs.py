from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever
from utils.answer_generator import generate_answer

documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

retriever = HybridRetriever(documents)

results = retriever.search(
    "What is the working hours?"
)

response = generate_answer(
    "What is the working hours?",
    results
)

print(response)