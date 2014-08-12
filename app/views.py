__author__ = 'ruslanpa'

import requests

from app import app
from flask import render_template
from utils import create_currencies, create_cities


@app.route("/")
@app.route("/index")
def index():
    context = requests.get('http://resources.finance.ua/ua/public/currency-cash.json')
    organizations = create_organizations(context.json())
    return render_template('index.html', title='Currencies', organizations=organizations)


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
