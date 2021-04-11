"""Example of launching Flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Main page"


@app.route('/<user>')
def user_page(user: str):
    return f"{user} page"


@app.route('/example-template')
def example_template():
    return render_template("html_example.html")


if __name__ == "__main__":
    app.run(debug=True)
