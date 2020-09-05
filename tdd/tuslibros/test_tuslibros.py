from unittest import TestCase


class TestTusLibros(TestCase):

    def test_shopping_cart_is_empty(self):
        new_shopping_cart = ShoppingCart()
        self.assertEquals(new_shopping_cart.getList(), [])
