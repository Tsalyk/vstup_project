"""
Module that connects HTML script with database analysis functions.
To start a website you need to run code from this module.
"""
import os
from flask import Flask, render_template, request, redirect, url_for
from tools import *


app = Flask(__name__)


@app.route("/ucu_chance", methods=['GET', 'POST'])
@app.route("/")
def index_page():
    """Render index page with info."""
    return render_template("index.html")


@app.route("/chance_calculator", methods=['GET', 'POST'])
def chance_page():
    """Render chance page with specialty selection"""

    specialties = ABIT.get_university_specialties()
    user_specialty = ""

    if request.method == 'POST':
        user_specialty = request.form.get('specialty')
        if not user_specialty:
            return render_template("chance.html", specialties=specialties)

        return redirect(url_for('calc', user_specialty=user_specialty))

    return render_template("chance.html", specialties=specialties)

@app.route("/calc")
def calc():
    """
    Generates a webpage with count of books and information
    table about all books for every given language.
    """
    universities = ["Український Католицький Університет"]
    specialties = ABIT.get_university_specialties()
    user_specialty = ""
    user_grades = ['', '', '', '']
    user_score = 0
    user_university = universities[0]
    user_percentage = "98 %"
    user_specialty = request.args.get('user_specialty')

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
    user_score = 0
    # user_score = ABIT.calculate_rating_grade(user_grades, exams_dict)
    if user_grades[0] and user_grades[1] and user_grades[2] and user_grades[3]:
        user_score = ABIT.calculate_rating_grade(user_grades, exams_dict)
    user_percentage = "98 %"

    return render_template("specialty.html", specialties=specialties, \
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