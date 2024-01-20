
from captions import get_captions
from chatGPT import get_summary

if __name__ == '__main__':

    url = ""

    transcript = get_captions(url)

    summary_and_search = get_summary(transcript)