from flask import Flask
from dotenv import load_dotenv

# Load enviroment
load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)

    from app.views import kamasutra
    app.register_blueprint(kamasutra)

    return app
