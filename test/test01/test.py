# -*- coding: UTF-8 -*-

# Python imports
import unittest

# Project imports
from lib_prices import *
from lib_settings import *
from portfolio import *


class JPMorganTestCase(unittest.TestCase):
    """Tests for 'portfolio.py'."""

    def test_01_portfolio_create_new(self):
        """Is portfolio create new returning a Portfolio instance?"""
        p = Portfolio.create_new(slug="test",
                                 description="Portfolio to be used in JPMorgan tests",
                                 user="automated unit tester",)
        self.assertTrue(isinstance(p, Portfolio),
                        msg="Portfolio was NOT successfully created")
        print("Portfolio '{}' - '{}' was successfully created by '{}' at '{}'".format(
            p.slug,
            p.description,
            p.created_by,
            p.created_at
        ))

        """Is portfolio create new not returning a Portfolio duplicated instance?"""
        p = Portfolio.create_new(slug="test",
                                 description="Portfolio to be used in JPMorgan tests AGAIN",
                                 user="automated unit tester",)
        self.assertFalse(isinstance(p, Portfolio),
                         msg="Duplicated portfolio was successfully created")
        print("Portfolio 'test' was NOT created AGAIN")

    def test_02_portfolio_get_all(self):
        """Is portfolio get all returning a list of Portfolio instances?"""
        self.assertTrue(isinstance(Portfolio.get_all(), list),
                        msg="Portfolio is NOT returning a list of all instances")
        print("Portfolio get_all method is returning the following list: {}".format(
            Portfolio.get_all(),
        ))

    def test_03_portfolio_get_specific_instance_by_slug(self):
        """Is portfolio get portfolio by slug returning an assertive instance?"""
        self.assertEqual(Portfolio.get_portfolio_by_slug("test"), Portfolio.get_all()[0],
                         msg="Portfolio is NOT returning a valid instance for a specific slug")
        print("Portfolio get_portfolio_by_slug method is returning the following instance: {}".format(
            Portfolio.get_portfolio_by_slug("test"),
        ))

    def test_04_insert_costs(self):
        """Is TransactionCost insert cost returning a valid instance?"""
        c_stock = TransactionCost.insert_new_cost(
            TRANSACTION_TYPE_STOCK, TRANSACTION_COST_FIXED, 5
        )
        c_bond = TransactionCost.insert_new_cost(
            TRANSACTION_TYPE_BOND, TRANSACTION_COST_VARIABLE, 0.01/100
        )
        c_cash = TransactionCost.insert_new_cost(
            TRANSACTION_TYPE_CASH, TRANSACTION_COST_FIXED, 0
        )

        self.assertTrue(isinstance(c_stock, TransactionCost),
                        msg="TransactionCost is NOT returning a valid inserted STOCK instance")
        print("TransactionCost insert STOCK cost is returning the following cost: {} - {}".format(
            TRANSACTION_COST_TYPES[c_stock.c_type][1],
            c_stock.factor,
        ))

        self.assertTrue(isinstance(c_bond, TransactionCost),
                        msg="TransactionCost is NOT returning a valid inserted BOND instance")
        print("TransactionCost insert BOND cost is returning the following cost: {} - {}".format(
            TRANSACTION_COST_TYPES[c_bond.c_type][1],
            c_bond.factor,
        ))

        self.assertTrue(isinstance(c_cash, TransactionCost),
                        msg="TransactionCost is NOT returning a valid inserted CASH instance")
        print("TransactionCost insert CASH cost is returning the following cost: {} - {}".format(
            TRANSACTION_COST_TYPES[c_cash.c_type][1],
            c_cash.factor,
        ))

    def test_05_transaction_create_buy_stock(self):
        """Is transaction creating valid buy stock objects?"""
        portfolio = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        buy_stock_aapl = Transaction.buy_stock(
            portfolio=portfolio,
            asset="AAPL",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=256,
            unit_price=162.94,
            user=user
        )

        buy_stock_ibm = Transaction.buy_stock(
            portfolio=portfolio,
            asset="IBM",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=128,
            unit_price=145.56,
            user=user
        )

        buy_stock_msft = Transaction.buy_stock(
            portfolio=portfolio,
            asset="MSFT",
            t_currency=TRANSACTION_CURRENCY_EUR,
            amount=64,
            unit_price=76.22,
            user=user
        )

        self.assertTrue(isinstance(buy_stock_aapl, Transaction),
                        msg="Transaction is NOT returning a valid object while buying an APPLE stock")
        print("Transaction buy_stock method is returning a valid APPLE transaction: {}".format(
            buy_stock_aapl))

        self.assertTrue(isinstance(buy_stock_ibm, Transaction),
                        msg="Transaction is NOT returning a valid object while buying an IBM stock")
        print("Transaction buy_stock method is returning a valid IBM transaction: {}".format(
            buy_stock_ibm))

        self.assertTrue(isinstance(buy_stock_msft, Transaction),
                        msg="Transaction is NOT returning a valid object while buying an MICROSOFT stock")
        print("Transaction buy_stock method is returning a valid MICROSOFT transaction: {}".format(
            buy_stock_msft))

    def test_06_get_all_portfolio_transactions(self):
        """Is portfolio get transactions returning a list of Transaction instances?"""
        p = Portfolio.get_portfolio_by_slug("test")
        t = Transaction.get_transactions(p)
        self.assertTrue(isinstance(t, list),
                        msg="Transaction is NOT returning a list of all transaction instances")
        print("Transaction get transactions is returning the following list: {}".format(
            t,
        ))

    def test_07_transaction_types_of_portfolio(self):
        """Is portfolio get transaction types returning an unique list of Transaction types?"""
        p = Portfolio.get_portfolio_by_slug("test")
        t = Transaction.get_transaction_types(p)
        self.assertTrue(isinstance(t, list),
                        msg="Transaction is NOT returning a list of unique transaction types")
        print("Transaction get transaction types is returning the following list: {}".format(
            t,
        ))

    def test_08_transaction_assets_of_portfolio(self):
        """Is portfolio get transaction assets returning an unique list of Transaction assets?"""
        p = Portfolio.get_portfolio_by_slug("test")
        t = Transaction.get_transaction_assets(p)
        self.assertTrue(isinstance(t, list),
                        msg="Transaction is NOT returning a list of unique transaction assets")
        print("Transaction get transaction assets is returning the following list: {}".format(
            t,
        ))

    def test_09_transactions_by_asset(self):
        """Is portfolio get transactions by asset returning a list of Transactions?"""
        p = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        buy_stock_ibm = Transaction.buy_stock(
            portfolio=p,
            asset="IBM",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=32,
            unit_price=144.96,
            user=user
        )

        t = Transaction.get_transactions_by_asset(p, "IBM")
        self.assertEqual(len(t), 2,
                         msg="Transaction is NOT returning a valid list of transaction by asset")
        print("Transaction get transactions by asset is returning the following list: {}".format(
            t,
        ))

    def test_10_insert_stock_prices(self):
        """Is Price insert asset price returning a valid instance?"""
        p_eur = Price.insert_new_price("EUR", 1.2)
        p_aapl = Price.insert_new_price("AAPL", 163.99)
        p_ibm = Price.insert_new_price("IBM", 145.78)
        p_msft = Price.insert_new_price("MSFT", 75.87)

        self.assertTrue(isinstance(p_eur, Price),
                        msg="Price is NOT returning a valid inserted EUR instance")
        print("Price insert EUR asset is returning the following price: {}".format(
            p_eur.price,
        ))

        self.assertTrue(isinstance(p_aapl, Price),
                        msg="Price is NOT returning a valid inserted AAPL instance")
        print("Price insert AAPL asset is returning the following price: {}".format(
            p_aapl.price,
        ))

        self.assertTrue(isinstance(p_ibm, Price),
                        msg="Price is NOT returning a valid inserted IBM instance")
        print("Price insert IBM asset is returning the following price: {}".format(
            p_ibm.price,
        ))

        self.assertTrue(isinstance(p_msft, Price),
                        msg="Price is NOT returning a valid inserted MSFT instance")
        print("Price insert MSFT asset is returning the following price: {}".format(
            p_msft.price,
        ))

    def test_11_transaction_create_sell_stock(self):
        """Is transaction creating valid sell stock objects?"""
        portfolio = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        sell_stock_aapl = Transaction.sell_stock(
            portfolio=portfolio,
            asset="AAPL",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=64,
            unit_price=163.04,
            user=user
        )

        sell_stock_msft = Transaction.sell_stock(
            portfolio=portfolio,
            asset="MSFT",
            t_currency=TRANSACTION_CURRENCY_EUR,
            amount=32,
            unit_price=76.20,
            user=user
        )

        self.assertTrue(isinstance(sell_stock_aapl, Transaction),
                        msg="Transaction is NOT returning a valid object while selling an AAPL stock")
        print("Transaction sell_stock method is returning a valid AAPL transaction: {}".format(
            sell_stock_aapl))

        self.assertTrue(isinstance(sell_stock_msft, Transaction),
                        msg="Transaction is NOT returning a valid object while selling an MSFT stock")
        print("Transaction sell_stock method is returning a valid MSFT transaction: {}".format(
            sell_stock_msft))

        """Is transaction avoiding short sell stock objects?"""
        short_sell_stock_msft = Transaction.sell_stock(
            portfolio=portfolio,
            asset="MSFT",
            t_currency=TRANSACTION_CURRENCY_EUR,
            amount=33,
            unit_price=78.20,
            user=user
        )

        self.assertFalse(isinstance(short_sell_stock_msft, Transaction),
                        msg="Transaction is NOT avoiding short selling an MSFT stock")
        print("Transaction sell_stock method is avoiding a short sell MSFT transaction: {}".format(
            short_sell_stock_msft))

    def test_12_transaction_create_buy_bond(self):
        portfolio = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        buy_bond_alitalia = Transaction.buy_bond(
            portfolio=portfolio,
            asset="ALITALIA",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=8,
            unit_price=120000,
            user=user
        )

        buy_bond_samsung = Transaction.buy_bond(
            portfolio=portfolio,
            asset="SAMSUNG",
            t_currency=TRANSACTION_CURRENCY_EUR,
            amount=4,
            unit_price=100000,
            user=user
        )

        self.assertTrue(isinstance(buy_bond_alitalia, Transaction),
                        msg="Transaction is NOT returning a valid object while buying an ALITALIA bond")
        print("Transaction buy_bond method is returning a valid ALITALIA transaction: {}".format(
            buy_bond_alitalia))

        self.assertTrue(isinstance(buy_bond_samsung, Transaction),
                        msg="Transaction is NOT returning a valid object while buying an SAMSUNG bond")
        print("Transaction buy_bond method is returning a valid SAMSUNG transaction: {}".format(
            buy_bond_samsung))

    def test_13_insert_bond_prices(self):
        """Is Price insert asset price returning a valid instance?"""
        p_alitalia = Price.insert_new_price("ALITALIA", 119000)
        p_samsung = Price.insert_new_price("SAMSUNG", 104000)

        self.assertTrue(isinstance(p_alitalia, Price),
                        msg="Price is NOT returning a valid inserted ALITALIA instance")
        print("Price insert ALITALIA asset is returning the following price: {}".format(
            p_alitalia.price,
        ))

        self.assertTrue(isinstance(p_samsung, Price),
                        msg="Price is NOT returning a valid inserted SAMSUNG instance")
        print("Price insert SAMSUNG asset is returning the following price: {}".format(
            p_samsung.price,
        ))

    def test_14_transaction_create_sell_bonds(self):
        """Is transaction creating valid sell bond objects?"""
        portfolio = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        sell_bond_alitalia = Transaction.sell_bond(
            portfolio=portfolio,
            asset="ALITALIA",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=8,
            unit_price=118000.04,
            user=user
        )

        self.assertTrue(isinstance(sell_bond_alitalia, Transaction),
                        msg="Transaction is NOT returning a valid object while selling an ALITALIA bond")
        print("Transaction sell_bond method is returning a valid ALITALIA transaction: {}".format(
            sell_bond_alitalia))

        """Is transaction avoiding short sell bond objects?"""
        short_sell_bond_alitalia = Transaction.sell_bond(
            portfolio=portfolio,
            asset="ALITALIA",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=1,
            unit_price=121000,
            user=user
        )

        self.assertFalse(isinstance(short_sell_bond_alitalia, Transaction),
                        msg="Transaction is NOT avoiding short selling an ALITALIA stock")
        print("Transaction sell_stock method is avoiding a short sell ALITALIA transaction: {}".format(
            short_sell_bond_alitalia))

    def test_15_transaction_create_buy_cash(self):
        portfolio = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        buy_cash_eur = Transaction.buy_cash(
            portfolio=portfolio,
            asset="EUR",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=200000,
            unit_price=1.15,
            user=user
        )

        buy_cash_usd = Transaction.buy_cash(
            portfolio=portfolio,
            asset="USD",
            t_currency=TRANSACTION_CURRENCY_EUR,
            amount=300000,
            unit_price=0.8547,
            user=user
        )

        self.assertTrue(isinstance(buy_cash_eur, Transaction),
                        msg="Transaction is NOT returning a valid object while buying EUR cash")
        print("Transaction buy_cash method is returning a valid EUR transaction: {}".format(
            buy_cash_eur))

        self.assertTrue(isinstance(buy_cash_usd, Transaction),
                        msg="Transaction is NOT returning a valid object while buying an USD cash")
        print("Transaction buy_cash method is returning a valid USD transaction: {}".format(
            buy_cash_usd))

    def test_16_insert_cash_prices(self):
        """Is Price insert asset price returning a valid instance?"""
        p_eur = Price.update_price("EUR", 1.17)
        p_usd = Price.insert_new_price("USD", 0.8909)

        self.assertTrue(isinstance(p_eur, Price),
                        msg="Price is NOT returning a valid inserted EUR instance")
        print("Price insert EUR asset is returning the following price: {}".format(
            p_eur.price,
        ))

        self.assertTrue(isinstance(p_usd, Price),
                        msg="Price is NOT returning a valid inserted USD instance")
        print("Price insert USD asset is returning the following price: {}".format(
            p_usd.price,
        ))

    def test_17_transaction_create_sell_cash(self):
        """Is transaction creating valid sell bond objects?"""
        portfolio = Portfolio.get_portfolio_by_slug("test")
        user = "automated unit tester"

        sell_cash_eur = Transaction.sell_cash(
            portfolio=portfolio,
            asset="EUR",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=100000,
            unit_price=1.17,
            user=user
        )

        self.assertTrue(isinstance(sell_cash_eur, Transaction),
                        msg="Transaction is NOT returning a valid object while selling EUR in cash")
        print("Transaction sell_cash method is returning a valid EUR transaction: {}".format(
            sell_cash_eur))

        """Is transaction avoiding short sell cash objects?"""
        short_sell_cash_eur = Transaction.sell_cash(
            portfolio=portfolio,
            asset="EUR",
            t_currency=TRANSACTION_CURRENCY_USD,
            amount=500000,
            unit_price=1.10,
            user=user
        )

        self.assertFalse(isinstance(short_sell_cash_eur, Transaction),
                        msg="Transaction is NOT avoiding short selling EUR in cash")
        print("Transaction sell_cash method is avoiding a short sell EUR transaction: {}".format(
            short_sell_cash_eur))

    def test_18_consolidate_portfolio(self):
        """Is Porfolio consolidation method returning a valid list of consolidated positions by asset?"""
        p = Portfolio.get_portfolio_by_slug("test")
        consolidations = Portfolio.consolidate_portfolio(p)
        self.assertTrue(isinstance(consolidations, list),
                        msg="Portfolio is NOT returning a valid consolidated list")
        print("Portfolio consolidate portfolio is returning the following list:")
        print("-" * 120)
        print("TYPE,ASSET,CURRENCY,BUY_AMOUNT,BUY_COST,SELL_AMOUNT,SELL_PROCEEDS,PNL_REALIZED_USD,PNL_REALIZED_EUR,"
              "REMAINING_POSITION,CURRENT_PRICE,CURRENT_VALUE_USD,CURRENT_VALUE_EUR,COST_AVERAGE,PNL_UNREALIZED_USD,"
              "PNL_UNREALIZED_EUR")
        for c in consolidations:
            c_row = []
            for _, v in c.items():
                c_row.append(str(v))

            print(",".join(c_row))


if __name__ == '__main__':
    unittest.main()
