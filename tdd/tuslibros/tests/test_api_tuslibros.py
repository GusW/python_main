from unittest import TestCase
from tuslibros.tuslibros_interface import TusLibrosInterfaceException
from tuslibros.shopping_cart import ShoppingCart
from tests.factory import TestFactory


class TestTusLibrosInterface(TestCase):
    def test_create_cart_with_valid_id(self):
        new_cart = TestFactory.create_new_interface_shopping_cart(
            TestFactory.A_VALID_CLIENT_ID,
            TestFactory.A_VALID_CLIENT_PASSWORD,
        )
        self.assertIsInstance(new_cart, ShoppingCart)

    def test_create_cart_with_invalid_id(self):
        with self.assertRaisesRegexp(Exception, TusLibrosInterfaceException.INVALID_CLIENT_ID.value):
            _ = TestFactory.create_new_interface_shopping_cart(
                TestFactory.A_INVALID_CLIENT_ID,
                TestFactory.A_VALID_CLIENT_PASSWORD,
            )

    def test_create_cart_with_invalid_password(self):
        with self.assertRaisesRegexp(Exception, TusLibrosInterfaceException.INVALID_CLIENT_PASSWORD.value):
            _ = TestFactory.create_new_interface_shopping_cart(
                TestFactory.A_VALID_CLIENT_ID,
                TestFactory.A_INVALID_CLIENT_PASSWORD,
            )

    def test_new_create_empty_cart(self):
        new_cart = TestFactory.create_new_interface_shopping_cart(
            TestFactory.A_VALID_CLIENT_ID,
            TestFactory.A_VALID_CLIENT_PASSWORD,
        )
        self.assertTrue(new_cart.isEmpty())

    def test_item_added_to_cart(self):
        cart_id = 10
        _ = TestFactory.create_new_interface_shopping_cart(
            client_id=TestFactory.A_VALID_CLIENT_ID,
            password=TestFactory.A_VALID_CLIENT_PASSWORD,
            cart_id=cart_id
        )
        new_interface = TestFactory.create_new_interface()
        self.assertEquals(new_interface.add_to_cart(cart_id, TestFactory.A_VALID_ISBN, 9),
                          "OK")
        self.assertEquals(new_interface.add_to_cart(cart_id, TestFactory.ANOTHER_VALID_ISBN, 5),
                          "OK")

        self.assertTrue(new_interface.list_cart(cart_id))
