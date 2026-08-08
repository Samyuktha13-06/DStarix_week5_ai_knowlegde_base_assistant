# pyrefly: ignore [missing-import]
from langchain_core.prompts import ChatPromptTemplate

query_transform_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert query rewriting assistant.

Rewrite the user's question so that it is:
- Clear
- Complete
- Retrieval-friendly
- Grammatically correct

Do NOT answer the question.

Only return the rewritten query.
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)