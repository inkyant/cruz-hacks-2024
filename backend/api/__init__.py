from flask import Flask
from flask_cors import CORS

def start_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    return app