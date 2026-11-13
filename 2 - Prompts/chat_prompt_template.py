# Used for multi-chat conversation

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are helpful {domain} expert'),
    ('human', 'Explain in simple term what is {topics}')
])

prompt = chat_template.invoke({"domain":"Cricket","topics":"Six"})

print(prompt)