from enum import Enum
from datetime import date


class CashierExceptionsEnum(str, Enum):
    CART_IS_EMPTY = 'Cannot checkout an empty cart'


class Cashier(object):
    def __init__(self,
                 shopping_cart=None,
                 credit_card=None,
                 date_benchmark=date.today()):
        self._validate_shopping_cart(shopping_cart)
        self._validate_credit_card(credit_card, date_benchmark)
        self._shopping_cart = shopping_cart
        self._credit_card = credit_card

    @property
    def shopping_cart(self):
        return self._shopping_cart

    @property
    def credit_card(self):
        return self._credit_card

    @staticmethod
    def _validate_shopping_cart(shopping_cart):
        if len(shopping_cart.cart) < 1:
            raise Exception(CashierExceptionsEnum.CART_IS_EMPTY.value)

    @staticmethod
    def _validate_credit_card(credit_card, date_benchmark):
        monthYear = credit_card.get('expiration')
        month, year = monthYear[:2], monthYear[2:]
        if (int(year) < int(date_benchmark.year)
            or (int(year) == int(date_benchmark.year)
                and int(month) < int(date_benchmark.month))):
            raise Exception(CashierExceptionsEnum.CART_IS_EMPTY.value)

    def checkout(self):
        totalCartPrice = 0.0
        for item in self._shopping_cart.cart:
            totalCartPrice += self._shopping_cart.publishing_house_catalog.get(
                item)

        return totalCartPrice
