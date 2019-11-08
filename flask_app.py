# export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import redirect
import os
from calculate_cost_form import CalculateCostForm

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
with open(PATH + "secrets.txt") as f:
    secret = f.read()
app.secret_key = secret


@app.route('/resultado')
def result():
    return render_template("success.html")

@app.route('/', methods=['GET', 'POST'])
def main():
    form = CalculateCostForm(request.form)
    if request.method == 'POST' and form.validate():

        print(form.km.data)
        print(form.peajes.data)
        print('front')
        print(form.frontera.data)
        flash('Thanks for registering') #TODO ver que hago con esto...

        return redirect(url_for('result'))
    return render_template("main.html", form=form)