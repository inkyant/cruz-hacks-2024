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
    
    summary = get_summary(transcript)
    return jsonify({"summary": summary})
