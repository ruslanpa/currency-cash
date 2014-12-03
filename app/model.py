__author__ = 'ruslanpa'


class Place(object):
    def __init__(self, **args):
        for name, value in args.items():
            if name == 'title':
                self.title = value
            elif name == 'address':
                self.address = value
            elif name == 'phone':
                self.phone = value
            elif name == 'cityId':
                self.cityId = value
            else:
                pass
        self.currencies = []
        self.city = 'undefined'


class Currency(object):
    def __init__(self, symbol, bid, ask):
        self.symbol = symbol
        self.bid = bid
        self.ask = ask

    def __str__(self):
        return "{} [{}, {}]".format(self.symbol, self.bid, self.ask)