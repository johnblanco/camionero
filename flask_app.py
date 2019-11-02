#export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello():
    return render_template("main.html")
