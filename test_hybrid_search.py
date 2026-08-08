from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever

documents = load_documents("documents/Internship Rule Book.pdf")

retriever = HybridRetriever(documents)

results = retriever.search(
    "Who is my mentor ?"
)

for i, doc in enumerate(results, 1):    

    print(f"\nResult {i}\n")

    print(doc.page_content)