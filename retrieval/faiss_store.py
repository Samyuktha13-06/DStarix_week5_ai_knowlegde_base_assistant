# pyrefly: ignore [missing-import]
from langchain_community.vectorstores import FAISS

from embeddings.embeddings import embedding_model


def create_faiss(documents):

    return FAISS.from_documents(
        documents,
        embedding_model
    )