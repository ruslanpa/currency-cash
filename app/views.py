__author__ = 'ruslanpa'

from app import app
from flask import render_template
from entities import Organization, Currency

import requests


@app.route("/")
@app.route("/index")
def index():
    context = requests.get('http://resources.finance.ua/ua/public/currency-cash.json')

    json_file = context.json()
    organizations = get_organizations(json_file)

    return render_template("index.html", title="Currencies", organizations=organizations)


def get_cities(json_file):
    cities = {}
    for i in json_file['cities']:
        cities[i] = json_file['cities'][i]
    return cities


def get_organizations(json_file):
    cities = get_cities(json_file)
    organizations = []
    for item in json_file['organizations']:
        organization = Organization(item['title'], item['address'], item['phone'])
        organization.currencies = get_currencies(item)
        organization.city = cities[item['cityId']]
        organizations.append(organization)
    return organizations


def get_currencies(json_file):
    currencies = []
    for i in json_file['currencies']:
        currency = Currency(i, json_file['currencies'][i]['ask'], json_file['currencies'][i]['bid'])
        currencies.append(currency)
    return currencies