__author__ = 'ruslanpa'

import requests
from flask import render_template, redirect

from app import app
from helpers import create_places


@app.route("/")
@app.route("/index")
def index():
    return redirect('/map')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', message=error), 404


@app.route("/map")
def show_map():
    context = requests.get('http://resources.finance.ua/ua/public/currency-cash.json')
    if context.status_code == 200:
        return render_template('map.html', places=create_places(context.json()))
    else:
        return render_template('404.html', message=context.reason)
