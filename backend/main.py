
from backend.api.captions import get_captions
from backend.api.chatGPT import get_summary

if __name__ == '__main__':

    url = "https://www.tiktok.com/@davisfang/video/7054881320974945537"

    transcript = get_captions(url)

    summary_and_search = get_summary(transcript)