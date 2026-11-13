from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="ibm-granite/granite-4.2-3b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Whats the matter with france lol")

print(result.content)