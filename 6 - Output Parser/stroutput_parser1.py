from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
# Prompt 1 → Creates the first prompt
#   ↓
# Model → Generates a response/report
#   ↓
# StrOutputParser → Converts the AI response into a plain string
#   ↓
# Prompt 2 → Uses the first response to create a summarization prompt
#   ↓
# Model → Generates the final summary
#   ↓
# StrOutputParser → Converts the final response into a plain string

result = chain.invoke({"topic":"Cricket"})

print(result)
