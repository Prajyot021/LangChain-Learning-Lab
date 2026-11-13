# we cant data validation here like if the output we got is input as we wanted or not

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import ( StructuredOutputParser, ResponseSchema )

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

Schema = [
    ResponseSchema(name="fact1", description ="Give me 1st fact about the topic"),
    ResponseSchema(name="fact2", description ="Give me 2nd fact about the topic"),
    ResponseSchema(name="fact3", description ="Give me 3rd fact about the topic")
]

parser = StructuredOutputParser.from_response_schemas(Schema)

template = PromptTemplate(
    template="Give me 3 facts about {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={'format_instructions':parser.get_format_instructions()}

)

chain = template | model | parser
result = chain.invoke({"topic":"cricket"})

print(result)