from evaluation.test_cases import test_cases

from loaders.document_loader import load_documents
from retrieval.hybrid_search import HybridRetriever
from utils.answer_generator import generate_answer


documents = load_documents(
    "documents/Internship Rule Book.pdf"
)

retriever = HybridRetriever(documents)


def evaluate():

    score = 0

    total = len(test_cases)

    print("=" * 80)

    print("LLM Evaluation Report")

    print("=" * 80)

    for test in test_cases:

        question = test["question"]

        expected = test["expected_keywords"]

        docs = retriever.search(question)

        response = generate_answer(
            question,
            docs
        )

        answer = response.answer.lower()

        passed = all(
            word.lower() in answer
            for word in expected
        )

        if passed:
            score += 1

        print(f"\nQuestion: {question}")

        print(f"Answer: {response.answer}")

        print(f"Confidence: {response.confidence}")

        print(
            "PASS"
            if passed
            else "FAIL"
        )

    print("\n")

    print(f"Score: {score}/{total}")