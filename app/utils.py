__author__ = 'ruslanpa'


def create_currencies(json_object):
    return {key: json_object[key] for key in json_object}


def create_cities(json_object):
    return {key: json_object['cities'][key] for key in json_object['cities']}