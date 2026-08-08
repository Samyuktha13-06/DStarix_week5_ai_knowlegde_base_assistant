from embeddings.embeddings import embedding_model

embeddings = embedding_model.embed_query(
    "Artificial Intelligence"
)

print(f"Embedding Dimension: {len(embeddings)}")
print(embeddings[:10])