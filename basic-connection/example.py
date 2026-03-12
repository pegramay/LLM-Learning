from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = OpenAI(base_url=os.getenv('LLM_URL'), api_key="lm-studio")

while True:
    x = input("ask me: ")
    print("=================================================================================")
    if x == "quit" or x =='q':
        break
    completion = client.chat.completions.create(
      model = os.getenv('LLM_MODEL'),
      messages=[
        {"role": "system", "content": "Always refer to me as 'sir fuego the wise' and every answer to a prompt must greet me."},
        {"role": "user", "content": x}
      ], #possible tweak this to look at objects instead of JSON format
      temperature=0.7, #Lower numbers more predictable, higher gives more creativity
      reasoning_effort="high",) 
    print(completion.choices[0].message.content)

