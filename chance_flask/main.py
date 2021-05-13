"""
Module that connects HTML script with database analysis functions.
To start a website you need to run code from this module.
"""
import os
from flask import Flask, render_template, request

TEMPLATE_DIR = os.path.abspath('./templates/')
STATIC_DIR = os.path.abspath('./statc/')


# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app = Flask(__name__)


@app.route("/ucu_chance", methods=['GET', 'POST'])
@app.route("/")
def index_page():
    """Render index page with info."""
    return render_template("index.html")


@app.route("/chance_calculator")
def country():
    """Render chance page with specialty selection"""
    return render_template("chance.html")


def launch_website():
    """
    Function that launches the website.
    """
    app.run(debug=True)
