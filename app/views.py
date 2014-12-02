__author__ = 'ruslanpa'

import requests
from flask import render_template, redirect

from app import app
from helpers import create_currencies, create_cities


@app.route("/")
@app.route("/index")
def index():
    return redirect('/map')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', message=error), 404


@app.route("/map")
def show_map():
    return render_template('map.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/filter")
def filter_currency():
    context = requests.get('http://resources.finance.ua/ua/public/currency-cash.json')
    if context.status_code == 200:
        return render_template('filter.html',
                               organizations=create_organizations(context.json()))
    else:
        return render_template('404.html')


def create_organizations(json_object):
    cities = create_cities(json_object)
    organizations = []
    for organization in json_object['organizations']:
        new_organization = Organization(cities, **organization)
        organizations.append(new_organization)
    return organizations


class Organization(object):

    def __init__(self, cities, **args):
        for name, value in args.items():
            if name == 'title':
                self.title = value
            elif name == 'address':
                self.address = value
            elif name == 'phone':
                self.phone = value
            elif name == 'currencies':
                self.currencies = create_currencies(value)
            elif name == 'cityId':
                self.city = cities[value]
