from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)


file_path = 'output.txt'


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/also.html")
def also():
    return render_template("also.html")


@app.route("/my_social.html")
def my_social():
    return render_template("my_social.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("bad_404.html"), 404




if __name__ == '__main__':
    app.run()
