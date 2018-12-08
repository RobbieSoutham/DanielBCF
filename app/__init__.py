from flask import Flask
import os
import yaml

path = os.path.dirname(__file__)
with open(path + "/config.yaml", 'r') as f: config = yaml.load(f)

# Creates our Flask application.
app = Flask(__name__)
app.config.update(
    static_url_path='/static',
    **config
)

import commands

from app import views, errors
