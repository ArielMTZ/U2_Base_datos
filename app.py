import os
from flask import Flask, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def inicio():
    return send_from_directory(BASE_DIR, "index.html")