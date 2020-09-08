from tuslibros.shopping_cart import ShoppingCart
from datetime import date, timedelta


class TestFactory(object):
    A_VALID_ISBN = 'validISBN'
    A_VALID_ISBN_PRICE = 10.65
    ANOTHER_VALID_ISBN = 'anotherValidISBN'
    ANOTHER_VALID_ISBN_PRICE = 10.65
    INVALID_ISBN = 'invalidISBN'

    @classmethod
    def get_publishing_house_catalog(cls):
        return {cls.A_VALID_ISBN: cls.A_VALID_ISBN_PRICE,
                cls.ANOTHER_VALID_ISBN: cls.ANOTHER_VALID_ISBN_PRICE}

    @classmethod
    def create_new_shopping_cart(cls):
        return ShoppingCart(publishing_house_catalog=cls.get_publishing_house_catalog())

    @classmethod
    def create_new_credit_card(cls, valid=True, date_benchmark=date.today()):
        credit_card = {
            'expiration': None,
        }
        if valid:
            valid_date = date_benchmark + timedelta(days=730)
            credit_card['expiration'] = valid_date.strftime("%m%Y")
        else:
            invalid_date = date_benchmark - timedelta(days=30)
            credit_card['expiration'] = invalid_date.strftime("%m%Y")

        return credit_card
