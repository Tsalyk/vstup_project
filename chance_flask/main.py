"""
Module that connects HTML script with database analysis functions.
To start a website you need to run code from this module.
"""
import os
from flask import Flask, render_template, request
# from tools import *

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
def chance_page():
    """Render chance page with specialty selection"""

    # Add result from a function instead of hardcode
    universities = ["Ukrainian Catholic University"]
    specialties = ["Artes Liberales", "Business Analytics", "Computer Science"]
    exams = ["MATHEMATICS", "UKRAINIAN", "ENGLISH", "GRADE"]
    info = [403, 50, 197.66, "75 000"]

    user_university = universities[0]
    user_specialty = specialties[2]
    user_score = 197.2
    user_percentage = "98 %"


    return render_template("chance.html", specialties=specialties, \
        universities=universities, exams=exams, info=info, user_score=user_score, \
        user_specialty=user_specialty, user_university=user_university, 
        user_percentage=user_percentage)


def launch_website():
    """
    Function that launches the website.
    """
    app.run(debug=True)
