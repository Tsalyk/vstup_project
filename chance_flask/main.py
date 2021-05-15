"""
Module that connects HTML script with database analysis functions.
To start a website you need to run code from this module.
"""
import os
from flask import Flask, render_template, request
from tools import *

TEMPLATE_DIR = os.path.abspath('./templates/')
STATIC_DIR = os.path.abspath('./statc/')


# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app = Flask(__name__)


@app.route("/ucu_chance", methods=['GET', 'POST'])
@app.route("/")
def index_page():
    """Render index page with info."""
    return render_template("index.html")


@app.route("/chance_calculator", methods=['GET', 'POST'])
def chance_page():
    """Render chance page with specialty selection"""

    universities = ["Український Католицький Університет"]
    specialties = ABIT.get_university_specialties()
    user_specialty = ""
    user_grades = [0, 0, 0, 0]

    if request.method == 'POST':
        user_specialty = request.form.get('specialty')

    exams = ABIT.get_exams_by_specialty(user_specialty)
    info = ABIT.get_info_by_specialty(user_specialty)

    if request.method == 'POST':
        exams = list(ABIT.get_exams_by_specialty(user_specialty).keys())
        grade_1 = request.form.get(exams[0])
        grade_2 = request.form.get(exams[1])
        grade_3 = request.form.get(exams[2])
        grade_4 = request.form.get(exams[3])

        user_grades = [grade_1, grade_2, grade_3, grade_4]
        print(user_grades)

    exams_dict = ABIT.get_exams_by_specialty(user_specialty)
    exams = list(exams_dict.keys())
    info = ABIT.get_info_by_specialty(user_specialty)


    user_university = universities[0]
    # user_score = ABIT.calculate_rating_grade(user_grades, exams)
    user_score = 100
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


if __name__ == '__main__':
    launch_website()