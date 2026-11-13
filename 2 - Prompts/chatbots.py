from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# chat_history=[   
# ]
# we do this if we wanna label it
chat_history = [
    SystemMessage(content="You are master in that field")
]
while True:
    user_input = input("User: ")

    chat_history.append(HumanMessage(content=user_input))
    # chat_history.append("User: " user_input)

    if user_input.lower() == "exit":
        break
    # Add user message with role
    # Send complete conversation history
    result = model.invoke(chat_history)

    # Add AI response with role
    ai_response = result.content[0]["text"]

    # print(result)
    # chat_history.append(("ai", ai_response))

    chat_history.append(AIMessage(content=ai_response))
    # chat_history.append("AI: " ai_response)


    print("AI:", ai_response)

print(chat_history)