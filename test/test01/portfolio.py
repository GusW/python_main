# -*- coding: UTF-8 -*-

# Python imports
import datetime
import collections
from functools import wraps

# Vendor imports

# Project imports
from lib_prices import Price
import lib_settings as lib
from collections import deque


class Portfolio:
    _instances = []

    def __init__(self, slug, description, user):
        self.slug = slug
        self.description = description
        self.created_by = user
        self.created_at = datetime.datetime.now()
        self.__class__._instances.append(self)

    @classmethod
    def create_new(cls, slug, description, user):
        """ considering portfolio's slug is our primary key/unique"""
        return cls(
            slug=slug,
            description=description,
            user=user,
        ) if not Portfolio.get_portfolio_by_slug(slug) else None

    @classmethod
    def get_all(cls):
        return cls._instances

    @classmethod
    def get_portfolio_by_slug(cls, slug):
        return ([portfolio for portfolio in cls.get_all() if portfolio.slug == slug][0] if
                [portfolio for portfolio in cls.get_all() if portfolio.slug == slug] else None)

    def consolidate_portfolio(self):
        t_types = (sorted(Transaction.get_transaction_types(self)) if
                   Transaction.get_transaction_types(self) else None)
        if t_types:
            p_consolidated = deque()
            total_pnl_realized_usd = total_pnl_realized_eur = 0
            total_pnl_unrealized_usd = total_pnl_unrealized_eur = 0
            total_current_value_usd = total_current_value_eur = 0
            for t in t_types:
                assets = Transaction.get_transaction_assets_by_type(self, t)
                for a in assets:
                    a_dict = collections.OrderedDict()
                    held, t_currency, buy_cost, buy_amount, sell_proceeds, sell_amount, pnl_realized_usd, \
                        pnl_realized_eur = Transaction.consolidate_position_by_asset(self, a)
                    current_price = Price.get_instance_price(a)
                    eur_exchange_rate = Price.get_instance_price("EUR")

                    a_dict["t_type"] = lib.TRANSACTION_TYPES[t][1]
                    a_dict["asset"] = a
                    a_dict["currency"] = lib.TRANSACTION_CURRENCIES[t_currency][1]
                    a_dict["buy_amount"] = buy_amount
                    a_dict["buy_cost"] = buy_cost
                    a_dict["sell_amount"] = sell_amount
                    a_dict["sell_proceeds"] = sell_proceeds
                    a_dict["pnl_realized_usd"] = pnl_realized_usd
                    a_dict["pnl_realized_eur"] = pnl_realized_eur
                    a_dict["remaining"] = held
                    a_dict["current_price"] = current_price.price
                    a_dict["current_value_usd"] = (held * current_price.price if
                                                   t_currency == lib.TRANSACTION_CURRENCY_USD else
                                                   held * current_price.price * eur_exchange_rate.price)
                    a_dict["current_value_eur"] = (held * current_price.price if
                                                   t_currency == lib.TRANSACTION_CURRENCY_EUR else
                                                   held * current_price.price / eur_exchange_rate.price)
                    a_dict["cost_average_per_share"] = buy_cost/buy_amount if buy_amount > 0 else 0
                    a_dict["pnl_unrealized_usd"] = (held * (current_price.price - (buy_cost/buy_amount)) if
                                                    t_currency == lib.TRANSACTION_CURRENCY_USD else
                                                    held * (current_price.price - (buy_cost/buy_amount)) *
                                                    eur_exchange_rate.price)
                    a_dict["pnl_unrealized_eur"] = (held * (current_price.price - (buy_cost/buy_amount)) if
                                                    t_currency == lib.TRANSACTION_CURRENCY_EUR else
                                                    held * (current_price.price - (buy_cost/buy_amount)) /
                                                    eur_exchange_rate.price)

                    p_consolidated.append(a_dict)

                    total_pnl_realized_usd += a_dict["pnl_realized_usd"]
                    total_pnl_realized_eur += a_dict["pnl_realized_eur"]
                    total_pnl_unrealized_usd += a_dict["pnl_unrealized_usd"]
                    total_pnl_unrealized_eur += a_dict["pnl_unrealized_eur"]
                    total_current_value_usd += a_dict["current_value_usd"]
                    total_current_value_eur += a_dict["current_value_eur"]

            p_dict = collections.OrderedDict()
            p_dict["t_type"] = "TOTAL"
            p_dict["asset"] = ""
            p_dict["currency"] = ""
            p_dict["buy_amount"] = ""
            p_dict["buy_cost"] = ""
            p_dict["sell_amount"] = ""
            p_dict["sell_proceeds"] = ""
            p_dict["pnl_realized_usd"] = total_pnl_realized_usd
            p_dict["pnl_realized_eur"] = total_pnl_realized_eur
            p_dict["remaining"] = ""
            p_dict["current_price"] = ""
            p_dict["current_value_usd"] = total_current_value_usd
            p_dict["current_value_eur"] = total_current_value_eur
            p_dict["cost_average_per_share"] = ""
            p_dict["pnl_unrealized_usd"] = total_pnl_unrealized_usd
            p_dict["pnl_unrealized_eur"] = total_pnl_unrealized_eur
            p_consolidated.append(p_dict)

            return p_consolidated


class Transaction:
    _instances = []

    def __init__(self, portfolio, t_type, t_operation, asset, t_currency, amount, unit_price, user,
                 realized_pnl_usd=None, realized_pnl_eur=None, cost=None):
        self.portfolio = portfolio
        self.t_type = t_type
        self.t_operation = t_operation
        self.asset = asset
        self.t_currency = t_currency
        self.amount = amount
        self.unit_price = unit_price
        self.cost = cost
        self.realized_pnl_usd = realized_pnl_usd
        self.realized_pnl_eur = realized_pnl_eur
        self.created_by = user
        self.created_at = datetime.datetime.now()
        self.__class__._instances.append(self)

    @staticmethod
    def get_all():
        return Transaction._instances

    @staticmethod
    def get_transactions_by_asset(portfolio, t_type, asset):
        return ([x for x in Transaction.get_all() if
                 x.portfolio == portfolio and x.t_type == t_type and x.asset == asset])

    # Short position decorator
    # Will be used on every sell transaciont to evaluate is there's no need to short sell an asset
    def evaluate_short_position(function):
        @wraps(function)
        def decorated(*args, **kwargs):
            portfolio = kwargs.get('portfolio')
            asset = kwargs.get('asset')
            amount = kwargs.get('amount')
            held, _, _, _, _, _, _, _ = Transaction.consolidate_position_by_asset(portfolio, asset)
            if held >= amount or lib.SHORT_SELL:
                return function(*args, **kwargs)

            return "Can NOT short sell: held {} and attempted {}".format(
                held, amount
            )

        return decorated

    @staticmethod
    def get_transactions(portfolio):
        return [x for x in Transaction.get_all() if x.portfolio == portfolio]

    @staticmethod
    def get_transaction_types(portfolio):
        return list(set([x.t_type for x in Transaction.get_transactions(portfolio) if x.portfolio == portfolio]))

    @staticmethod
    def get_transaction_assets(portfolio):
        return list(set([x.asset for x in Transaction.get_transactions(portfolio) if x.portfolio == portfolio]))

    @staticmethod
    def get_transaction_assets_by_type(portfolio, t_type):
        return list(set([x.asset for x in Transaction.get_transactions(portfolio) if x.portfolio == portfolio and
                         x.t_type == t_type]))

    @staticmethod
    def get_transactions_by_asset(portfolio, asset):
        if asset in Transaction.get_transaction_assets(portfolio):
            return ([x for x in Transaction.get_all() if x.portfolio == portfolio and
                     x.asset == asset])

        return None

    @staticmethod
    def get_cost_average(portfolio, asset):
        buy_amount = buy_cost = 0
        transactions = Transaction.get_transactions_by_asset(portfolio, asset)
        for t in transactions:
            if t.t_operation == lib.TRANSACTION_OPERATION_BUY:
                buy_amount += t.amount
                buy_cost += (t.amount * t.unit_price) + \
                    (t.cost if t.cost is not None else 0)

        return buy_cost/buy_amount if buy_amount > 0 else 0

    @staticmethod
    def consolidate_position_by_asset(portfolio, asset):
        held = realized_pnl_usd = realized_pnl_eur = 0
        buy_amount = sell_amount = 0
        buy_cost = sell_proceeds = 0
        transactions = Transaction.get_transactions_by_asset(portfolio, asset)
        for t in transactions:
            if t.t_operation == lib.TRANSACTION_OPERATION_BUY:
                held += t.amount
                buy_amount += t.amount
                buy_cost += (t.amount * t.unit_price) + \
                    (t.cost if t.cost is not None else 0)
            else:
                held -= t.amount
                realized_pnl_usd += t.realized_pnl_usd
                realized_pnl_eur += t.realized_pnl_eur
                sell_amount += t.amount
                sell_proceeds += (t.amount * t.unit_price) - \
                    (t.cost if t.cost is not None else 0)

        return held, t.t_currency, buy_cost, buy_amount, sell_proceeds, sell_amount, realized_pnl_usd, realized_pnl_eur

    @staticmethod
    def calculated_realized_pnl(portfolio, asset, amount, unit_price, cost):
        average_cost = Transaction.get_cost_average(portfolio, asset)
        return (amount * (unit_price - average_cost)) - cost

    @staticmethod
    def buy_stock(portfolio, asset, t_currency, amount, unit_price, user):
        t = Transaction(
            portfolio=portfolio,
            t_type=lib.TRANSACTION_TYPE_STOCK,
            t_operation=lib.TRANSACTION_OPERATION_BUY,
            asset=asset,
            t_currency=t_currency,
            amount=amount,
            unit_price=unit_price,
            user=user,
        )
        t.cost = TransactionCost.calculate_cost(t)
        return t

    @staticmethod
    @evaluate_short_position
    def sell_stock(portfolio, asset, t_currency, amount, unit_price, user):
        t = Transaction(
            portfolio=portfolio,
            t_type=lib.TRANSACTION_TYPE_STOCK,
            t_operation=lib.TRANSACTION_OPERATION_SELL,
            asset=asset,
            t_currency=t_currency,
            amount=amount,
            unit_price=unit_price,
            user=user,
        )
        t.cost = TransactionCost.calculate_cost(t)
        realized_pnl = Transaction.calculated_realized_pnl(
            portfolio=portfolio,
            asset=asset,
            amount=amount,
            unit_price=unit_price,
            cost=t.cost
        )
        t.realized_pnl_usd = (realized_pnl if t_currency == lib.TRANSACTION_CURRENCY_USD else
                              realized_pnl * Price.get_instance_price("EUR").price)
        t.realized_pnl_eur = (realized_pnl if t_currency == lib.TRANSACTION_CURRENCY_EUR else
                              realized_pnl / Price.get_instance_price("EUR").price)
        return t

    @staticmethod
    def buy_bond(portfolio, asset, t_currency, amount, unit_price, user):
        t = Transaction(
            portfolio=portfolio,
            t_type=lib.TRANSACTION_TYPE_BOND,
            t_operation=lib.TRANSACTION_OPERATION_BUY,
            asset=asset,
            t_currency=t_currency,
            amount=amount,
            unit_price=unit_price,
            user=user,
        )
        t.cost = TransactionCost.calculate_cost(t)
        return t

    @staticmethod
    @evaluate_short_position
    def sell_bond(portfolio, asset, t_currency, amount, unit_price, user):
        t = Transaction(
            portfolio=portfolio,
            t_type=lib.TRANSACTION_TYPE_BOND,
            t_operation=lib.TRANSACTION_OPERATION_SELL,
            asset=asset,
            t_currency=t_currency,
            amount=amount,
            unit_price=unit_price,
            user=user,
        )
        t.cost = TransactionCost.calculate_cost(t)
        realized_pnl = Transaction.calculated_realized_pnl(
            portfolio=portfolio,
            asset=asset,
            amount=amount,
            unit_price=unit_price,
            cost=t.cost
        )
        t.realized_pnl_usd = (realized_pnl if t_currency == lib.TRANSACTION_CURRENCY_USD else
                              realized_pnl * Price.get_instance_price(lib.TRANSACTION_CURRENCY_EUR).price)
        t.realized_pnl_eur = (realized_pnl if t_currency == lib.TRANSACTION_CURRENCY_EUR else
                              realized_pnl / Price.get_instance_price(lib.TRANSACTION_CURRENCY_EUR).price)
        return t

    @staticmethod
    def buy_cash(portfolio, asset, t_currency, amount, unit_price, user):
        t = Transaction(
            portfolio=portfolio,
            t_type=lib.TRANSACTION_TYPE_CASH,
            t_operation=lib.TRANSACTION_OPERATION_BUY,
            asset=asset,
            t_currency=t_currency,
            amount=amount,
            unit_price=unit_price,
            user=user,
        )
        t.cost = TransactionCost.calculate_cost(t)
        return t

    @staticmethod
    @evaluate_short_position
    def sell_cash(portfolio, asset, t_currency, amount, unit_price, user):
        t = Transaction(
            portfolio=portfolio,
            t_type=lib.TRANSACTION_TYPE_CASH,
            t_operation=lib.TRANSACTION_OPERATION_SELL,
            asset=asset,
            t_currency=t_currency,
            amount=amount,
            unit_price=unit_price,
            user=user,
        )
        t.cost = TransactionCost.calculate_cost(t)
        realized_pnl = Transaction.calculated_realized_pnl(
            portfolio=portfolio,
            asset=asset,
            amount=amount,
            unit_price=unit_price,
            cost=t.cost
        )
        t.realized_pnl_usd = (realized_pnl if t_currency == lib.TRANSACTION_CURRENCY_USD else
                              realized_pnl * Price.get_instance_price("EUR").price)
        t.realized_pnl_eur = (realized_pnl if t_currency == lib.TRANSACTION_CURRENCY_EUR else
                              realized_pnl / Price.get_instance_price("EUR").price)
        return t


class TransactionCost:
    _instances = []

    def __init__(self, t_type, c_type, factor):
        self.t_type = t_type
        self.c_type = c_type
        self.factor = factor
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.__class__._instances.append(self)

    @staticmethod
    def get_all_costs():
        return TransactionCost._instances

    @staticmethod
    def get_instance_cost(t_type):
        return ([x for x in TransactionCost.get_all_costs() if x.t_type == t_type][0] if
                len([x for x in TransactionCost.get_all_costs() if x.t_type == t_type]) > 0 else None)

    @classmethod
    def insert_new_cost(cls, t_type, c_type, factor):
        if not TransactionCost.get_instance_cost(t_type):
            return cls(
                t_type=t_type,
                c_type=c_type,
                factor=factor,
            )

        return None

    @staticmethod
    def update_cost(t_type, c_type, factor):
        transaction_cost = TransactionCost.get_instance_cost(t_type)
        if len(transaction_cost) > 0:
            transaction_cost.c_type = c_type
            transaction_cost.factor = factor
            transaction_cost.updated_at = datetime.datetime.now()
            return transaction_cost

        return None

    @staticmethod
    def calculate_cost(transaction):
        transaction_cost = TransactionCost.get_instance_cost(transaction.t_type)
        if transaction_cost is not None:
            return (transaction_cost.factor if transaction_cost.c_type == lib.TRANSACTION_COST_FIXED else
                    transaction.amount * transaction.unit_price * transaction_cost.factor)

        return 0
