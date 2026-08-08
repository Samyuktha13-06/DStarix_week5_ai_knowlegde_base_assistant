from utils.llm import llm

response = llm.invoke(
    "Explain what Retrieval-Augmented Generation is."
)

print(response.content)
