# pyrefly: ignore [missing-import]
from pydantic import BaseModel


class AnswerResponse(BaseModel):

    answer: str

    confidence: str

    found_in_documents: bool