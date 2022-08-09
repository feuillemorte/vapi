"""Small vulnerable API. WARNING: DO NOT USE THIS API IN PRODUCTION!"""
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_smorest import Api

from . import db
from .blueprints import pets


handler = RotatingFileHandler("app.log", maxBytes=1000000, backupCount=5)

db.init()
app = Flask(__name__)

handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
log = logging.getLogger("werkzeug")
log.setLevel(logging.DEBUG)
log.addHandler(handler)

app.config["API_TITLE"] = "Small vulnerable API (DO NOT USE IN PRODUCTION)"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_JSON_PATH"] = "openapi.json"
app.config["OPENAPI_URL_PREFIX"] = "/docs"
app.config["API_SPEC_OPTIONS"] = {"servers": [{"url": "http://127.0.0.1:5000/"}]}
api = Api(app)

api.register_blueprint(pets.pets_blueprint)
