from flask import Blueprint, jsonify, request
from .captions import get_captions
from .chatGPT import get_summary

routes = Blueprint("routes", __name__)

@routes.route("/api/fact-check", methods=['POST'])
def fact_check():
    url = request.get_json()

    if not url:
        return {}
    
    transcript = get_captions(url)
    if not transcript:
        return {}

    s = get_summary(transcript)
    match = re.match(r'(.+?)\n\nSearch Terms:(.+)', s)
    if (match is None):
        print("Error on  match regex")
        return jsonify({"summary": s, "terms": ""})
    return jsonify({"summary": match.group(1), "terms": match.group(1)})

