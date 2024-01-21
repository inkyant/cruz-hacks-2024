import asyncio
from .image_cap import video_caption
from .api_keys import ASM_AI_API_KEY
import assemblyai as aai
import pyktok as pyk
import os
import csv
from datetime import datetime
# import glob
import re

pyk.specify_browser('chrome')
aai.settings.api_key = ASM_AI_API_KEY
pattern = r"https://(?:www\.)?tiktok.com/([^?]+)"

async def get_captions(url):
    cwd = os.getcwd()
    video_path = ""

    match = re.search(pattern, url)
    if match:
        video_name = match.group(1).replace("/", "_")
        video_path = os.path.join(cwd, video_name + ".mp4")
        csv_path = os.path.join(cwd, video_name + ".csv")
    else:
        return None, None, None
    
    try:
        pyk.save_tiktok(url, True, csv_path)
    except TypeError:
        return None, None, None

    transcriber = aai.Transcriber()
    metadata = dict()
    try:
        
        # get transcript of audio
        async def transcribe():
            return transcriber.transcribe(video_path).text

        # get video transcript
        async def vid_transcribe():
            return await video_caption(video_path)
        
        transcript, video_transcript = await asyncio.gather(transcribe(), vid_transcribe())


        with open(csv_path) as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                metadata["description"] = row["video_description"]
                metadata["date"] = str(datetime.strptime(row["video_timestamp"], "%Y-%m-%dT%H:%M:%S").date())
            print(metadata)
        os.remove(csv_path)
        os.remove(video_path)
    except FileNotFoundError:
        return None, None, None
    return transcript, video_transcript, metadata
