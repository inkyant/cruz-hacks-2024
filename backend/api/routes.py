import re
from flask import Blueprint, jsonify, request

from .snopes_check import query_snopes
from .captions import get_captions
from .chatGPT import get_summary, get_article

routes = Blueprint("routes", __name__)

@routes.route("/api/fact-check", methods=['POST'])
def fact_check():
    url = request.get_json()

    if not url:
        return {}
    
    transcript, video_transcript, metadata = get_captions(url)
    if not transcript:
        return {}

    s = get_summary(transcript, video_transcript, metadata["description"], metadata["date"])

    print("\n" + "="*8)
    print(s)
    print("\n" + "="*8)

    match = re.match(r'(.+?)\n\n?Search Terms:(.+)', s)
    if (match is None):
        print("Error on match regex")
        return jsonify({"summary": s, "terms": "", "description": metadata["description"], "date": metadata["date"]})
    
    search_terms = match.group(2)  
    search_terms = search_terms.replace(",", "")

    article_selected = ""

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
        
    return jsonify({"summary": match.group(1), "snopes": article_selected})
    