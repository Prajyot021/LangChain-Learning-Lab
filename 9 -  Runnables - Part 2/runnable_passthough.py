from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt1 = PromptTemplate(
    template="Give me a joke on the {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Explain the joke :-{text}',
    input_variables=['text']
)

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explain':RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generator, parallel_chain)

result = final_chain.invoke({'topic':'cricket'})

print(result)