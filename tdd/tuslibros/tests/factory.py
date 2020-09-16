from datetime import date, timedelta
from enum import Enum
from credit_card import CreditCard
from cashier import Cashier
from merchant_processor import MerchantProcessor
from shopping_cart import ShoppingCart
from tuslibros_interface import TusLibrosInterface


class TestFactory(object):
    A_VALID_ISBN = 'validISBN'
    A_VALID_ISBN_PRICE = 10.65
    ANOTHER_VALID_ISBN = 'anotherValidISBN'
    ANOTHER_VALID_ISBN_PRICE = 10.65
    INVALID_ISBN = 'invalidISBN'
    A_VALID_CLIENT_ID = 'validID'
    A_INVALID_CLIENT_ID = 'invalidID'
    A_VALID_CLIENT_PASSWORD = 'validPassword'
    A_INVALID_CLIENT_PASSWORD = 'invalidPassword'


    @classmethod
    def get_publishing_house_catalog(cls):
        return {cls.A_VALID_ISBN: cls.A_VALID_ISBN_PRICE,
                cls.ANOTHER_VALID_ISBN: cls.ANOTHER_VALID_ISBN_PRICE}

    @classmethod
    def create_cart(cls):
        return ShoppingCart(publishing_house_catalog=cls.get_publishing_house_catalog())

    @classmethod
    def create_new_credit_card(cls, valid=True, date_benchmark=date.today()):
        targetDate = (date_benchmark + timedelta(days=730)
                      if valid
                      else date_benchmark - timedelta(days=30))

        return CreditCard(expiration_date=targetDate)

    @classmethod
    def create_new_cashier(cls,
                           shopping_cart=None,
                           credit_card=None,
                           merchant_processor=None):
        return Cashier(shopping_cart=shopping_cart or cls.create_cart(),
                       credit_card=credit_card or cls.create_new_credit_card(),
                       merchant_processor=merchant_processor or cls.create_new_merchant_processor())

    @classmethod
    def create_new_merchant_processor(cls, message_builder=None):
        return MerchantProcessor(message_builder=message_builder or MessageBuilderStubSuccess)

    @classmethod
    def get_user_source(cls):
        return{
            cls.A_VALID_CLIENT_ID: cls.A_VALID_CLIENT_PASSWORD,
        }

    @classmethod
    def create_new_interface(cls, user_source=None):
        return TusLibrosInterface(
            user_source=cls.get_user_source()
        )

    @classmethod
    def create_new_interface_shopping_cart(cls,
                                           client_id=None,
                                           password=None,
                                           cart_id=None):
        interface = cls.create_new_interface()
        return interface.create_cart(
            client_id=client_id or cls.A_INVALID_CLIENT_ID,
            client_password=password or cls.A_INVALID_CLIENT_PASSWORD,
            publishing_house_catalog=cls.get_publishing_house_catalog(),
            cart_id=cart_id or 1
        )


class MessageBuilderResponses(str, Enum):
    UNAVAILABLE_MP = 'Merchant Processor is unavailable'
    NO_CREDIT_FUNDS = 'Credit Card has not enough funds'


class MessageBuilderStub(object):
    def debit(credit_card, amount):
        raise NotImplementedError('Must be subclass responsability')


class MessageBuilderStubUnavailableMP(MessageBuilderStub):
    def debit(credit_card, amount):
        raise Exception(MessageBuilderResponses.UNAVAILABLE_MP.value)


class MessageBuilderStubNoCreditFunds(MessageBuilderStub):
    def debit(credit_card, amount):
        raise Exception(MessageBuilderResponses.NO_CREDIT_FUNDS.value)


class MessageBuilderStubSuccess(MessageBuilderStub):
    def debit(credit_card, amount):
        return 'TRANSACTION_ID'
