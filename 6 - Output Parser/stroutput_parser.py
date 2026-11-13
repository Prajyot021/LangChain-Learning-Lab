from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# as we can see, we did it normally here without any output parser.
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Give me report on the {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="""
Summarize the following text in EXACTLY 5 lines.

Rules:
- Write exactly 5 lines.
- Each line should contain one concise sentence.
- Do not add a title.
- Do not add extra explanations.

Text:
{text}
""",
    input_variables=["text"]
)
# prompt2 has to be that good since llms sometimes cant understand exactly what we want.

a1 = prompt1.invoke({"topic":"black holes"})
# a1= prompt1.format() - it works same as .invoke
content1 = model.invoke(a1)

a2 = prompt2.invoke({"text":content1.content})
content2 = model.invoke(a2)

print(content2.content)
