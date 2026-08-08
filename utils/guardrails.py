# pyrefly: ignore [missing-import]
from langchain_core.prompts import ChatPromptTemplate

guardrail_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Knowledge Base Assistant.

Answer ONLY from the provided context.

Rules:

1. Never invent information.
2. Never use outside knowledge.
3. If the answer is unavailable, clearly say so.

Return ONLY valid JSON.

Required JSON format:

{{
  "answer": "...",
  "confidence": "high | medium | low",
  "found_in_documents": true
}}
"""
        ),
        (
            "human",
            """
Context:

{context}

Question:

{question}
"""
        )
    ]
)