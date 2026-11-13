from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt1 = PromptTemplate(
    template="Give me a joke on the {topic}",
    input_variables='topic'
)
prompt2 = PromptTemplate(
    template='Explain the joke :-{text}',
    input_variables='text'
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke('Ram')
print(result)