from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = OpenAI(base_url=os.getenv('LLM_URL'), api_key="lm-studio")


completion = client.chat.completions.create(
  model = os.getenv('LLM_MODEL'),
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
