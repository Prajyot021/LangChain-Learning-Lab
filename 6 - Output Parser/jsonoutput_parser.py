from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    # template="Give me name, age and city of a fictional character \n {format_instruction}",
    template = "Give me 5 dark facts about {text}", # if we want to give some input
    # input_variables=[],
    input_variables =['text'],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# print(result.content)

# or we can just create a chain

chain = template | model |parser
# result = chain.invoke({}) # we gotta give an empty dictionay if we arnet giving an input
result = chain.invoke("Ram from Ramayan")

print(result)
print(type(result))

# we cant force an schema upon json output. It will give as LLM desired