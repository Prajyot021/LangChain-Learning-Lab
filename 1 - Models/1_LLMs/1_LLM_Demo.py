from langchain_openai import OpenAI
from dotenv import load_dotenv 
# this is used to import enviroment variable/api keys from .env file like for openAI one here. Its not here since its not free

load_dotenv()  # Load environment variables/API key here from .env file

llm = OpenAI(model_name="gpt-4")  # Initialize the LLM Object with the model name and temperature. Temperature is a hyperparameter that controls the randomness of the model's output. A higher temperature will result in more random outputs, while a lower temperature will result in more deterministic outputs. Maax_completetion_token is the maximum number of tokens that the model can generate in a single response. The default value is 2048, but it can be increased or decreased based on the use case. 

result = llm.invoke("What is the capital of France?")  # Call the LLM Object with a prompt and store the result in a variable.

print(result)  # Print the result to the console.