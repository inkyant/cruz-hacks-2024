from api_keys import ASM_AI_API_KEY
import assemblyai as aai

aai.settings.api_key = ASM_AI_API_KEY

transcriber = aai.Transcriber()
link = "https://v39-eu.tiktokcdn.com/6d4f8b635601721b3f8644f83c11497a/65abbcf6/video/tos/maliva/tos-maliva-ve-0068c799-us/ooEI4dLVdQGfHegATSyAesIsLVIsjuSIqUGWaC/?a=1180&ch=0&cr=13&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=2740&bt=1370&bti=OHYpOTY0Zik3OjlmOm01MzE6ZDQ0MDo%3D&cs=2&ds=4&ft=XsdJEquYm3FPD12QEH-R3wUIK~c7aeF~O5&mime_type=video_mp4&qs=15&rc=PDpmZzU6OTU0PGhmNGg8ZUBpamg4OHk5cnJlcDMzaTczNEA0MDBgYC0wXmMxLzU0XzA1YSNobGVfMmRzMWlgLS1kMTJzcw%3D%3D&l=20240120062942EC0EB3FA7217861FBDB2&btag=e00095000"
transcript = transcriber.transcribe(link)
print(transcript.text)