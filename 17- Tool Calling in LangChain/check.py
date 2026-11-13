import os
import requests
from dotenv import load_dotenv
from typing import Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

# 1. Define tools with proper error handling and environment variables
@tool
def conversion_rate(base_currency: str, target_currency: str) -> float:
    """Fetches the currency conversion factor between base and target currency."""
    api_key = os.getenv("967ab55646c462eacda33415")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if "conversion_rate" not in data:
        raise ValueError(f"API Error: {data.get('error-type', 'Unknown error')}")
    return data["conversion_rate"]

# 2. Bind tools
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
llm_with_tools = model.bind_tools([conversion_rate])

# 3. Message sequence execution
messages = [HumanMessage('What is the conversion factor between USD and INR, and based on that can you convert 10 inr to usd')]

# First model invocation
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)  # CRITICAL: Append AIMessage first

# Execute returned tool calls
for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'conversion_rate':
        tool_output = conversion_rate.invoke(tool_call['args'])
        messages.append(
            ToolMessage(
                content=str(tool_output),
                tool_call_id=tool_call['id']
            )
        )

# Final model invocation with complete history
final_response = llm_with_tools.invoke(messages)
print(final_response.content)