from pyshorteners import Shortener


class Service:
    def __call__(self, data: dict):
        shortener = Shortener()
        return shortener.tinyurl.short(data['link'])
