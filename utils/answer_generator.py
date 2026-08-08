import json

from utils.guardrails import guardrail_prompt
from utils.llm import llm
from utils.schema import AnswerResponse


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

    data = json.loads(
        response.content
    )

    return AnswerResponse(**data)