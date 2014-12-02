__author__ = 'ruslanpa'


class Place(object):
    currencies = []
    city = 'undefined'

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


class Currency(object):
    def __init__(self, bid_ask=None):
        if not bid_ask:
            bid_ask = []
        self.bid_ask = bid_ask

    def bid(self):
        if self.__bid_ask_exist():
            return self.bid_ask[0]
        else:
            return 0

    def ask(self):
        if self.__bid_ask_exist():
            return self.bid_ask[-1]
        else:
            return 0

    def __bid_ask_exist(self):
        return len(self.bid_ask) == 2