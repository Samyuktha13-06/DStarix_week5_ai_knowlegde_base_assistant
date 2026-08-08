from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever

documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

retriever = HybridRetriever(documents)

results = retriever.search(
    "Who is the mentor?"
)

print("\nTop Ranked Documents:\n")

for i, doc in enumerate(results, 1):

    print(f"Result {i}\n")

    print(doc.page_content)

    print("-" * 80)