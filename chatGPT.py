
from api_keys import OPEN_AI_API_KEY

from openai import OpenAI

client = OpenAI(api_key=OPEN_AI_API_KEY)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")