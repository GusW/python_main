from unittest import TestCase

from tuslibros.tests.factory import TestFactory
from tuslibros.shopping_cart import ShoppingCartExceptionsEnum


class TestPurchase(TestCase):
    def setUp(self):
        self.valid_ISBN = TestFactory.A_VALID_ISBN
        self.another_valid_ISBN = TestFactory.ANOTHER_VALID_ISBN
        self.invalid_ISBN = TestFactory.INVALID_ISBN
        self.new_shopping_cart = TestFactory.create_cart()

    def tearDown(self):
        super(TestPurchase, self).tearDown()

    def test_shopping_cart_is_empty_after_creation(self):
        self.assertEquals(len(self.new_shopping_cart.cart), 0)

    def test_shopping_cart_is_not_empty_after_add_book_to_empty_cart(self):
        self.new_shopping_cart.add(self.valid_ISBN)
        self.assertGreater(len(self.new_shopping_cart.cart), 0)

    def test_shopping_cart_is_not_empty_after_add_several_books_to_empty_cart(self):
        isbn_qty = 5
        self.new_shopping_cart.add(self.another_valid_ISBN, qty=isbn_qty)

        self.assertGreater(len(self.new_shopping_cart.cart), 0)
        self.assertEquals(self.new_shopping_cart.get_book_qty(
            self.another_valid_ISBN), isbn_qty)

    def test_cannot_add_book_that_does_not_belong_to_the_publishing_house(self):
        with self.assertRaisesRegexp(Exception, ShoppingCartExceptionsEnum.ISBN_NOT_IN_CATALOG.value):
            self.new_shopping_cart.add(self.invalid_ISBN, qty=1)

        self.assertEquals(len(self.new_shopping_cart.cart), 0)

    def test_cannot_add_book_whose_quantity_is_less_than_one(self):
        with self.assertRaisesRegexp(Exception, ShoppingCartExceptionsEnum.QUANTITY_LESS_THAN_ONE.value):
            self.new_shopping_cart.add(self.invalid_ISBN, qty=0)

        self.assertEquals(len(self.new_shopping_cart.cart), 0)
