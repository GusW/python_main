from enum import Enum
from datetime import date


class CashierExceptionsEnum(str, Enum):
    CART_IS_EMPTY = 'Cannot checkout an empty cart'
    EXPIRED_CREDIT_CARD = 'Credit Card is expired - cannot proceed to payment'


class Cashier(object):
    def __init__(self,
                 shopping_cart=None,
                 credit_card=None,
                 date_benchmark=date.today(),
                 merchant_processor=None):
        self._validate_shopping_cart(shopping_cart)
        self._validate_credit_card(credit_card, date_benchmark)
        self._shopping_cart = shopping_cart
        self._credit_card = credit_card
        self._merchant_processor = merchant_processor

    @property
    def shopping_cart(self):
        return self._shopping_cart

    @property
    def credit_card(self):
        return self._credit_card

    @property
    def merchant_processor(self):
        return self._merchant_processor

    @staticmethod
    def _validate_shopping_cart(shopping_cart):
        if len(shopping_cart.cart) < 1:
            raise Exception(CashierExceptionsEnum.CART_IS_EMPTY.value)

    @staticmethod
    def _validate_credit_card(credit_card, date_benchmark=date.today()):
        if credit_card._is_credit_card_expired(date_benchmark):
            raise Exception(CashierExceptionsEnum.EXPIRED_CREDIT_CARD.value)

    def calculateTotalAmount(self):
        totalCartPrice = 0.0
        for item in self._shopping_cart.cart:
            totalCartPrice += self._shopping_cart.publishing_house_catalog.get(
                item)

        return totalCartPrice

    def checkout(self):
        totalAmount = self.calculateTotalAmount()
        self.merchant_processor.debit(self.credit_card,
                                      self.calculateTotalAmount())
        return totalAmount
