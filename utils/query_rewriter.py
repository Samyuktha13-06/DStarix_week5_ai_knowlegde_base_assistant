from prompts.query_transform import query_transform_prompt
from utils.llm import llm


def rewrite_query(question: str) -> str:

    chain = query_transform_prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content.strip()