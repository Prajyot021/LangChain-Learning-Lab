# claude and openAI isnt free. This is somehow free. You can get a free api key from google cloud console. This is a demo of how to use the google gemini model with langchain.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# this is how gemini's api key is imported from .env file.

load_dotenv()  # Load environment variables/API key here from .env file

llm = ChatGoogleGenerativeAI(model="gemini-flash-latest")

result  = llm.invoke("why do you exist?")  # Call the LLM Object with a prompt and store the result in a variable.

print(result.text)  # Print the result to the console.

# | Model ID                 | Type    | Input limit | Output limit | Best for                              |
# | ------------------------ | ------- | ----------: | -----------: | ------------------------------------- |
# | `gemini-3.7-flash`       | Stable  |          1M |       65,536 | Best overall Flash, coding, agents    |
# | `gemini-3.6-flash`       | Stable  |          1M |       65,536 | Strong general-purpose model          |
# | `gemini-3.5-flash`       | Stable  |          1M |       65,536 | Routine workloads                     |
# | `gemini-3.5-flash-lite`  | Stable  |          1M |       65,536 | **Fastest/high-volume general tasks** |
# | `gemini-3.1-flash-lite`  | Stable  |          1M |       65,536 | Cheap and efficient                   |
# | `gemini-3.1-pro-preview` | Preview |          1M |       65,536 | Complex reasoning                     |
# | `gemini-3-flash-preview` | Preview |          1M |       65,536 | Older Gemini 3 Flash preview          |
# | `gemini-2.5-flash`       | Stable  |          1M |       65,536 | Older general-purpose Flash           |
# | `gemini-2.5-flash-lite`  | Stable  |          1M |       65,536 | Older lightweight Flash               |
# | `gemini-2.5-pro`         | Stable  |          1M |       65,536 | Strong reasoning                      |
