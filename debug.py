import ipdb
from lib.book import Book
from lib.coffee import Coffee

cradle = Book("Cradle", 200)
latte = Coffee(size="Large", price=3.50)

if __name__ == '__main__':
    ipdb.set_trace()
