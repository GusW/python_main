# -*- coding: UTF-8 -*-

# Python imports
import datetime
from collections import deque


class AssetPrice:
    _instances = deque()

    def __init__(self, asset, price):
        self.asset = asset
        self.price = price
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.__class__._instances.append(self)

    @staticmethod
    def get_prices():
        return AssetPrice._instances

    @staticmethod
    def get_asset_price(asset):
        asset_price_list = [p for p in AssetPrice.get_prices() if p.asset == asset]
        if len(asset_price_list) > 0:
            return asset_price_list[0]

        raise UnknownAssetPriceException('{} not found in database'.format(asset))
            
    @classmethod
    def insert_new_price(cls, asset, price):
        if not cls.get_asset_price(asset):
            return cls(
                asset=asset,
                price=price
            )
        
        raise PreexistingAssetPriceException('There is already an AssetPrice named {} in database'.format(asset))
    
    # should be property?
    def update_asset_price(self, asset = None, price = None):
        self.asset = asset if asset else self.asset
        self.price = price if price else self.price
        self.updated_at = datetime.datetime.now()
