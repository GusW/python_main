# -*- coding: UTF-8 -*-

# Python imports
import datetime
from collections import deque


class Price:
    _instances = deque()

    def __init__(self, asset, price):
        self.asset = asset
        self.price = price
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.__class__._instances.append(self)

    @staticmethod
    def get_all_prices():
        return Price._instances

    @staticmethod
    def get_instance_price(asset):
        return ([x for x in Price.get_all_prices() if x.asset == asset][0] if
                len([x for x in Price.get_all_prices() if x.asset == asset]) > 0 else None)

    @classmethod
    def insert_new_price(cls, asset, price):
        if not Price.get_instance_price(asset):
            return cls(
                asset=asset,
                price=price
            )

        return None

    @staticmethod
    def update_price(asset, price):
        asset_price = Price.get_instance_price(asset)
        if asset_price is not None:
            asset_price.price = price
            asset_price.updated_at = datetime.datetime.now()
            return asset_price

        return None
