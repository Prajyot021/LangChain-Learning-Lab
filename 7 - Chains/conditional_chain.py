from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser1 = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['Positive','Negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the feedback into positive or negative \n {feedback} \n{format_instruction}',
    input_variables='feedback',
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classfication_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'Give  me appropriate response for this positive feedback \n {feedback}',
    input_variables='feedback'
)
prompt3 = PromptTemplate(
    template = 'Give  me appropriate response for this negative feedback \n {feedback}',
    input_variables='feedback'
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='Positive', prompt2|model|parser1),
    (lambda x:x.sentiment=='Negative', prompt3|model|parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classfication_chain | branch_chain

result= chain.invoke({'feedback':"This is a terrible phone"})
print(result)


