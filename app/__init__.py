from flask import Flask
import os
import yaml

PATH = os.path.dirname(__file__)
CONFIG = PATH + "/configs/{}.yaml".format(
    os.environ.get("FLASK_ENV",)
)

# Creates our Flask application.
app = Flask(__name__)

with open(CONFIG, "r") as config: 
    app.config.update(
        **yaml.load(config)
    )

from app import views, errors