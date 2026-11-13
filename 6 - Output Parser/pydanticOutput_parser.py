# stringoutput parser - for string output
# json output parser - but doesnt enforces schema
# structured output parser - it do enforce schema but doenst do validation
# pydantic output parser - structured json+ validation
# there are also parsers as well but these are most used.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class p1(BaseModel):
    name:str=Field(description="Name of the person")
    age:int = Field(description="Age of the person")
    city:str = Field(description="Location of the person")

parser = PydanticOutputParser(pydantic_object=p1)

template = PromptTemplate(
    template="name, age, palce of a {place} fictional character \n {format_instruction}",
    input_variables={'place'},
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# content1 = template.invoke({"place":"indian"})
# result = model.invoke(content1)
# final_result = parser.parse(result.content)
# print(final_result)

# or using chains
chain = template | model | parser
result = chain.invoke({'place':"indian"})
print(result)

