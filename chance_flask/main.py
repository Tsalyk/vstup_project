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

@app.route("/calc", methods=['GET', 'POST'])
def calc():
    """
    Generates a webpage with count of books and information
    table about all books for every given language.
    """
    user_university = "Український Католицький Університет"
    user_specialty = request.args.get('user_specialty')

    info = ABIT.get_info_by_specialty(user_specialty)
    exams = ABIT.get_exams_by_specialty(user_specialty)
    exams_list = list(exams.keys())

    user_grades = ['', '', '', '']
    user_score = 0
    user_percentage = "?"

    if request.method == 'POST':
        grade_1 = request.form.get(exams_list[0])
        grade_2 = request.form.get(exams_list[1])
        grade_3 = request.form.get(exams_list[2])
        grade_4 = request.form.get(exams_list[3])

        user_grades = [grade_1, grade_2, grade_3, grade_4]
        print(user_grades)

        user_score = round(ABIT.calculate_rating_grade(user_grades, exams), 2)
        user_percentage = ABIT.calculate_chance(user_score, user_specialty)

    return render_template("specialty.html", user_university=user_university, user_grades=user_grades, 
    user_specialty=user_specialty, exams=exams_list, info=info, user_score=user_score, user_percentage=user_percentage)

def launch_website():
    """
    Function that launches the website.
    """
    app.run(debug=True)


if __name__ == '__main__':
    launch_website()