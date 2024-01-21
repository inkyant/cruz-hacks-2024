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

def get_captions(url):
    cwd = os.getcwd()
    video_path = ""

    match = re.search(pattern, url)
    if match:
        video_name = match.group(1).replace("/", "_")
        video_path = os.path.join(cwd, video_name + ".mp4")
        csv_path = os.path.join(cwd, video_name + ".csv")
    else:
        return None
    
    try:
        pyk.save_tiktok(url, True, csv_path)
    except TypeError:
        return None

    transcriber = aai.Transcriber()
    metadata = dict()
    try:
        transcript_obj = transcriber.transcribe(video_path)
        transcript = transcript_obj.text
        with open(csv_path) as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                metadata["description"] = row["video_description"]
                metadata["date"] = str(datetime.strptime(row["video_timestamp"], "%Y-%m-%dT%H:%M:%S").date())
            print(metadata)
        os.remove(csv_path)
        os.remove(video_path)
    except FileNotFoundError:
        return None
    return transcript, metadata