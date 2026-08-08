from utils.query_rewriter import rewrite_query

question = "How many WFH days do employees get?"

print("Original Question:\n")
print(question)

print("\nRewritten Question:\n")
print(rewrite_query(question))