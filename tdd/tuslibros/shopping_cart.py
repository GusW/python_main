from enum import Enum


class ShoppingCartExceptionsEnum(str, Enum):
    CART_IS_EMPTY = 'Cannot checkout an empty cart'
    ISBN_NOT_IN_CATALOG = 'Book does not belong to the publishing house'
    QUANTITY_LESS_THAN_ONE = 'Cannot add book whose quantity is less than 1'


class ShoppingCart(object):
    def __init__(self, publishing_house_catalog=()):
        self._cart = {}
        self._publishing_house_catalog = publishing_house_catalog

    @property
    def cart(self):
        return self._cart

    @property
    def publishing_house_catalog(self):
        return self._publishing_house_catalog

    def isEmpty(self):
        return len(self.cart) == 0

    def add(self, isbn, qty=1):
        if qty < 1:
            raise Exception(ShoppingCartExceptionsEnum.QUANTITY_LESS_THAN_ONE.value)
        elif isbn in self.publishing_house_catalog:
            preexisting_qty = self._cart.get(isbn, 0)
            self._cart[isbn] = preexisting_qty + qty
        else:
            raise Exception(ShoppingCartExceptionsEnum.ISBN_NOT_IN_CATALOG.value)

    def get_book_qty(self, book_isbn):
        return self.cart.get(book_isbn, 0)
