__author__ = 'ruslanpa'

import requests
from flask import render_template

from app import app
from utils import create_currencies, create_cities


@app.route("/")
@app.route("/index")
def index():
    context = requests.get('http://resources.finance.ua/ua/public/currency-cash.json')
    if context.status_code == 200:
        return render_template('index.html',
                               title='Currencies',
                               organizations=create_organizations(context.json()))
    else:
        return render_template('404.html', title='Page not found')


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
