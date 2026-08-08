from utils.llm import llm
from utils.guardrails import guardrail_prompt


def generate_answer(question, documents):

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    chain = guardrail_prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content