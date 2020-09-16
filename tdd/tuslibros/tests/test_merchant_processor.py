from unittest import TestCase
from tuslibros.tests.factory import (TestFactory,
                                     MessageBuilderResponses,
                                     MessageBuilderStubUnavailableMP,
                                     MessageBuilderStubNoCreditFunds)


class TestMerchantProcessor(TestCase):
    def setUp(self):
        self.new_shopping_cart = TestFactory.create_cart()

    def test_merchant_processor_unavailable(self):
        merchant_processor = TestFactory.create_new_merchant_processor(MessageBuilderStubUnavailableMP)
        self.new_shopping_cart.add(TestFactory.A_VALID_ISBN)
        cashier = TestFactory.create_new_cashier(
            shopping_cart=self.new_shopping_cart,
            merchant_processor=merchant_processor)
        with self.assertRaisesRegex(Exception, MessageBuilderResponses.UNAVAILABLE_MP.value):
            cashier.checkout()

    def test_no_credit_card_funds(self):
        merchant_processor = TestFactory.create_new_merchant_processor(
            MessageBuilderStubNoCreditFunds)
        self.new_shopping_cart.add(TestFactory.A_VALID_ISBN)
        cashier = TestFactory.create_new_cashier(
            shopping_cart=self.new_shopping_cart,
            merchant_processor=merchant_processor)
        with self.assertRaisesRegex(Exception, MessageBuilderResponses.NO_CREDIT_FUNDS.value):
            cashier.checkout()

    def test_successful_checkout(self):
        merchant_processor = TestFactory.create_new_merchant_processor()
        self.new_shopping_cart.add(TestFactory.A_VALID_ISBN)
        cashier = TestFactory.create_new_cashier(
            shopping_cart=self.new_shopping_cart,
            merchant_processor=merchant_processor)
        self.assertEqual(cashier.checkout(), cashier.calculateTotalAmount())
