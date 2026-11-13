from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


documents = [
    "Virat Kohli is one of the most successful batters in modern cricket and has scored over 80 international centuries.",

    "Sachin Tendulkar is the only player to score 100 international centuries. He is widely regarded as one of the greatest batters in cricket history.",

    "MS Dhoni led India to victory in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy.",
    
    "Ricky Ponting is one of Australia's most successful cricket captains and won two ODI World Cups as captain.",

    "AB de Villiers was known for his innovative shots and ability to bat in almost any position."
]

questions = "What is achieved by Villiers in cricket?"

vector_embed = embeddings.embed_documents(documents)
query_embed = embeddings.embed_query(questions)

cosine_similarities = cosine_similarity([query_embed], vector_embed)[0]

print(cosine_similarities)