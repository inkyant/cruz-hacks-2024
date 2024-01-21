import re
from .api_keys import OPEN_AI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPEN_AI_API_KEY)

def get_summary(transcript, video_transcript, description, date):

    prompt = """Imagine you are an independent body that has to release a short summary of misinformation present within a video. The video transcript provided  below will be the video for which you will highlight any misinformation present, in just 3 sentences.
Additionally, after those three sentences, if there is misinformation present, create a line break and type \"Search Terms:\" and then exactly 7 search terms that could be used to get specific information about the topic. Do not type anything else on that line, and do not type this line if there is not a lot of misinformation. Only type one search query. Only type 7 words, do not include commas or multiple searches. For example:
\"Search Terms: flat earth theory 2020 proven with gravity\"\nThe video was posed on """ + date + " and has this description: \"" + description +"\". In the video frames, this occurs: " + video_transcript + " Here is the audio transcript: " 

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt + "\n" + transcript}],
        stream=False,
    )

    print("="*8)
    print(prompt + "\n" + transcript)
    print("="*8)

    # print(response.choices[0].message.content)
    if response.choices:
        return response.choices[0].message.content
    # for res in response.choices:
    #     if (re.match(r'unable to provide information', res.message.content or "") is None):
    #         return res.message.content


def get_article(transcript: str, articles: str):
    prompt1 = """Consider this video transcript that may contain misinformation:"""
    prompt2 = """Choose the most relevant of these snopes articles to the topic in the transcript. Respond with just one number, or -1 if none apply. For example, your response could be:1"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt1 + "\n" + transcript + "\n" + prompt2 + "\n" + articles}],
        stream=False,
    )

    print(response.choices[0].message)

    try:
        if response.choices[0].message.content is not None:
            return int(response.choices[0].message.content)
        else:
            print("message content is none")
    except ValueError:
        print("chatGPT did not return a number")