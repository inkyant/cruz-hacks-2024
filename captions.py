from api_keys import ASM_AI_API_KEY
import assemblyai as aai
import pyktok as pyk
import os
# import glob
import re

pyk.specify_browser('chrome')
aai.settings.api_key = ASM_AI_API_KEY

def get_captions(url):
    pattern = r"https://(?:www.)?tiktok.com/(.+)"

    cwd = os.getcwd()
    video_path = ""

    match = re.search(pattern, url)
    if match:
        video_name = match.group(1).replace("/", "_") + ".mp4"
        video_path = os.path.join(cwd, video_name)
    else:
        return None
    
    try:
        pyk.save_tiktok(url)
    except TypeError:
        return None

    transcriber = aai.Transcriber()
    try:
        transcript_obj = transcriber.transcribe(video_path)
        transcript = transcript_obj.text
        os.remove(video_path)
    except FileNotFoundError:
        return None
    return transcript