from api_keys import OPEN_AI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPEN_AI_API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=False,
)

print(response.choices[0].message)