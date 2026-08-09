from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever
from utils.answer_generator import generate_answer

print("=" * 60)
print("AI Knowledge Base Assistant")
print("Type 'exit' to quit")
print("=" * 60)

# Load documents once
documents = load_documents("documents/Internship Rule Book.pdf")
retriever = HybridRetriever(documents)

while True:

    question = input("\nYou: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    if not question:
        print("Please enter a question.")
        continue

    docs = retriever.search(question)

    response = generate_answer(question, docs)

    print("\nAssistant:")
    print(response.answer)
    print(f"\nConfidence: {response.confidence}")