from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a linkedin post about {topic}',
    input_variable= ['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'post':RunnableSequence(prompt2, model, parser)
})
# RunnableParallel takes a single input and passes it simultaneously to multiple runnables. The results are returned as a dictionary using the keys you defined.
         
result = chain.invoke({'topic':'AI'})
# print(result)
print(result['tweet'])
print(result['post'])
