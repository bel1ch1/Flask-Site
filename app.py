from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

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


def buttonLike():
    with open('button_logs.txt', 'a') as file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'Button pressed at {timestamp}\n')
    return 'Button press logged'

if __name__ == '__main__':
    app.run()
