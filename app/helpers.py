__author__ = 'ruslanpa'

from app.model import Place, Currency


def create_places(data):
    places = []
    for organization in data['organizations']:
        new_place = Place(**organization)
        new_place.city = data['cities'][new_place.cityId]
        if organization['currencies']:
            for c in organization['currencies'].items():
                currency = Currency(c[0], c[1]['bid'], c[1]['ask'])
                new_place.currencies.append(currency)
        places.append(new_place)
    return places