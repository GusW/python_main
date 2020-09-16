from tuslibros.shopping_cart import ShoppingCart
from enum import Enum


class TusLibrosInterfaceException(Enum):
    INVALID_CLIENT_ID = 'Invald client ID'
    INVALID_CLIENT_PASSWORD = 'Invalid client password'


class TusLibrosInterface(object):

    SHOPPING_CART_LIST = {}

    def __init__(self,
                 user_source=None):
        self._user_source = user_source or {}

    @property
    def user_source(self):
        return self._user_source

    def check_user(self, username):
        return username in self.user_source

    def check_password(self, client_id, client_password):
        return self.user_source.get(client_id) == client_password

    def _validate_client_info(self, client_id, client_password):
        if not self.check_user(client_id):
            raise Exception(TusLibrosInterfaceException.INVALID_CLIENT_ID.value)

        if not self.check_password(client_id, client_password):
            raise Exception(TusLibrosInterfaceException.INVALID_CLIENT_PASSWORD.value)

    def create_cart(self,
                    client_id=None,
                    client_password=None,
                    publishing_house_catalog=None,
                    cart_id=None):
        self._validate_client_info(client_id, client_password)
        new_shopping_cart = ShoppingCart(publishing_house_catalog=publishing_house_catalog)
        self.SHOPPING_CART_LIST[cart_id] = new_shopping_cart
        return new_shopping_cart

    def _get_cart_by_id(self, cart_id):
        return self.SHOPPING_CART_LIST.get(cart_id)

    def add_to_cart(self,
                    cart_id,
                    book_isbn,
                    book_qty):

        shopping_cart = self._get_cart_by_id(cart_id)
        if shopping_cart:
            shopping_cart.add(book_isbn, book_qty)
            return "OK"

    def list_cart(self, cart_id):
        shopping_cart = self._get_cart_by_id(cart_id)
        if shopping_cart:
            list_of_isbn_qty = [(k, v) for k, v in shopping_cart.cart.items()]
            return '|'.join([f"{ISBN}|{QTY}" for ISBN, QTY in list_of_isbn_qty])
