# i didnt run it since it will download it

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline(
    repo_id = "ibm-granite/granite-4.2-3b",
    task = "text-generation",

    pipeline_kwargs= dict{
        temperature=0.5,
        max_length=100,
    }
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("Whats the matter with france lol")

print(result.content)