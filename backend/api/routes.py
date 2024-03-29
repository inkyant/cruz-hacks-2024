import asyncio
import re
from flask import Blueprint, jsonify, request
import time

from .snopes_check import query_snopes
from .captions import get_captions
from .chatGPT import get_summary, get_article

routes = Blueprint("routes", __name__)

@routes.route("/api/fact-check", methods=['POST'])
def fact_check():
    start = time.time()
    url = request.get_json()

    if not url:
        return {}
    
    transcript, video_transcript, metadata = None, None, None

    try:
        transcript, video_transcript, metadata = asyncio.get_running_loop().run_until_complete(get_captions(url))
    except RuntimeError:
        transcript, video_transcript, metadata = asyncio.run(get_captions(url))
        
    if not transcript:
        return {}

    s = get_summary(transcript, video_transcript, metadata["description"], metadata["date"])

    print("\n" + "="*8)
    print(s)
    print("\n" + "="*8)

    match = re.match(r'(.+?)\n\n?Search Terms:(.+)', s)
    if (match is None):
        print("Error on match regex")
        end = time.time()
        print(f"Runtime: {end-start} seconds")
        return jsonify({"summary": s, "terms": ""})
    
    search_terms = match.group(2)  
    search_terms = search_terms.replace(",", "")

    article_selected = ""
    article_link = ""

    if search_terms and not (re.match(r'.*N/A.*', search_terms) or re.match(r'.*None.*', search_terms)):
        
        print("Searching snopes for: " + search_terms)

        articles = query_snopes(search_terms)

        articles_str = ""
        for i, a in enumerate(articles):
            articles_str += str(i)
            articles_str += a["title"]
            articles_str += "\n"
            articles_str += a["byline"]
            articles_str += "\n"
        
        article_id = get_article(transcript, articles_str)

        print("\n" + "="*8)
        print(articles_str)
        print("\n" + "="*8)
        print(article_id)
        print("\n" + "="*8)
        print("\n\n")

        if article_id is not None and article_id != -1:
            article_selected = articles[article_id]["title"]
            article_link = articles[article_id]["link"]
    end = time.time()
    print(f"Runtime: {end-start} seconds")
        
    return jsonify({"summary": match.group(1), "snopes": article_selected, "snopes_link": article_link})
    