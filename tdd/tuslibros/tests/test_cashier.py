from unittest import TestCase
from tuslibros.cashier import Cashier, CashierExceptionsEnum
from tuslibros.tests.factory import TestFactory
from datetime import date


class TestCheckout(TestCase):
    def setUp(self):
        self.new_shopping_cart = TestFactory.create_new_shopping_cart()
        self.invalid_credit_card = TestFactory.create_new_credit_card(valid=False, date_benchmark=date.today())
        self.valid_credit_card = TestFactory.create_new_credit_card()
        self.valid_ISBN = TestFactory.A_VALID_ISBN
        self.valid_ISBN_price = TestFactory.A_VALID_ISBN_PRICE

    def tearDown(self):
        super(TestCheckout, self).tearDown()

    def test_cannot_checkout_with_empty_cart(self):
        with self.assertRaisesRegexp(Exception, CashierExceptionsEnum.CART_IS_EMPTY.value):
            _ = Cashier(shopping_cart=self.new_shopping_cart)

    def test_chekout_cart_calculates_debit_amount(self):
        self.new_shopping_cart.add(self.valid_ISBN)
        expected_cart_price_sum = self.valid_ISBN_price
        new_cashier = Cashier(
            shopping_cart=self.new_shopping_cart, credit_card=self.valid_credit_card)
        self.assertEquals(new_cashier.checkout(), expected_cart_price_sum)

    def test_not_possible_to_checkout_with_expired_credit_card(self):
        self.new_shopping_cart.add(self.valid_ISBN, 9)
        with self.assertRaisesRegexp(Exception, CashierExceptionsEnum.CART_IS_EMPTY.value):
            _ = Cashier(shopping_cart=self.new_shopping_cart, credit_card=self.invalid_credit_card)
