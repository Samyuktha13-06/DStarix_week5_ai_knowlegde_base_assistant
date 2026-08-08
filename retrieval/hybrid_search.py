from retrieval.faiss_store import create_faiss
from retrieval.bm25_store import create_bm25
from retrieval.reranker import Reranker


class HybridRetriever:

    def __init__(self, documents):

        self.faiss = create_faiss(documents)

        self.bm25 = create_bm25(documents)

        self.reranker = Reranker()

    def search(self, query):

        faiss_docs = self.faiss.similarity_search(
            query,
            k=5
        )

        bm25_docs = self.bm25.invoke(query)

        combined = []

        seen = set()

        for doc in faiss_docs + bm25_docs:

            if doc.page_content not in seen:

                combined.append(doc)

                seen.add(doc.page_content)

        return self.reranker.rerank(
            query,
            combined,
            top_k=3
        )