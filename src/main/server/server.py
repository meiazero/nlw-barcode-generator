from flask import Flask
from src.main.routes.tag import tag

app = Flask(__name__)

app.register_blueprint(tag)
