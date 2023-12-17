from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/also.html")
def also():
    return render_template("also.html")


@app.route("/my_social.html")
def my_social():
    return render_template("my_social.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("bg_404.html")


if __name__ == "__main__":
    app.run(debug=True)
