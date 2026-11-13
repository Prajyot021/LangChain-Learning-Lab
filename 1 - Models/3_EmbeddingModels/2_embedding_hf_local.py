from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "What is the capital of France?"

documents=[
    "The capital of France is Paris.",
    "France is a country in Europe.",
    "The Eiffel Tower is located in Paris.",
]

# vector = embeddings.embed_query(text)

vector = embeddings.embed_documents(documents)


print(vector)