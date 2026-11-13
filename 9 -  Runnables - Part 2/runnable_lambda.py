from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Give me a small dark fact about {topic}',
    input_variables=['topic']
)

facts = RunnableSequence(prompt, model, parser)

def word_count(facts):
    return len(facts.split())

parallel_chain = RunnableParallel({
    'fact':RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain= RunnableSequence(facts, parallel_chain)
result = final_chain.invoke({'topic':'Ramayan'})

print(result)