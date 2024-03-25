import os
from dotenv import load_dotenv
from brave import Brave
import json 
import gpt

# Your Brave API key
load_dotenv(dotenv_path='components/.env')
api_key = os.getenv("brave_key")

brave = Brave(api_key)

query = "Quel temps il fait aujourd'hui?"
num_results = 10

search_results = brave.search(q=query, count=num_results)

web_results = search_results.web_results

brave_input = ''
for i in web_results:
    brave_input += "\n" + i['description']

#print(brave_input)
print(gpt.openai_request(query,''))
print(gpt.openai_request(query,brave_input))