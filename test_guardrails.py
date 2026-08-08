from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever
from utils.answer_generator import generate_answer

documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

retriever = HybridRetriever(documents)

query = "What is the salary structure?"

results = retriever.search(query)

answer = generate_answer(
    query,
    results
)

print(answer)