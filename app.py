import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from flask import Flask, send_from_directory
from routes.api_routes import api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)

    @app.route("/")
    def home():
        return send_from_directory(".", "index.html")

    @app.route("/panel")
    def panel():
        return send_from_directory(".", "panel.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)