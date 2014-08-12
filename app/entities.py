__author__ = 'ruslanpa'


class Organization(object):
    def __init__(self, title, address, phone):
        self.title = title
        self.address = address
        self.phone = phone
        self.currencies = []
        self.city = "UNDEFINED"

    def contact_info(self):
        return " ".join([self.city, self.address])


class Currency(object):
    def __init__(self, id, ask, bid):
        self.id = id
        self.ask = ask
        self.bid = bid

    def info(self):
        """
        Gets full info of currency
        :return: a string representation of currency
        """
        return " ".join([self.id, "[ask: {0}, bid: {1}]".format(self.ask, self.bid)])