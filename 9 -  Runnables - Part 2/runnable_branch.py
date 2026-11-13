from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarise and do mention its summarsied in beginning the following - {text}',
    input_variables=['text']
)

# report = RunnableSequence(prompt1, model,parser)
# or since its same thing but only for RunnableSequence. Its called LCLE (Langchain expression language)
report = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain= RunnableSequence(report, branch_chain)
result = final_chain.invoke({'topic':'Cricket'})

print(result)