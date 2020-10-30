
from myCompany.db_interfaces.shop import ShopDBInterface, ShopOfflineAvailabilityDBInterface
from myCompany.resources.shop import Shop
from myCompany.services.common import BaseService


class ShopService(BaseService):
    def __init__(self, db_connector, batch_date) -> None:
        super().__init__(db_connector, batch_date)
        self._interface_shop = self._create_new_shop_interface()
        self._interface_availability = self._create_new_availability_interface()

    @property
    def interface_shop(self):
        ''' interface_shop getter method '''
        return self._interface_shop

    @property
    def interface_availability(self):
        ''' interface_availability getter method '''
        return self._interface_availability

    def _create_new_shop_interface(self):
        ''' Creates a new ShopDBInterface given the received db_connector '''
        return ShopDBInterface(self.db_connector)

    def _create_new_availability_interface(self):
        ''' Creates a new ShopAvailabilityDBInterface given the received db_connector '''
        return ShopOfflineAvailabilityDBInterface(self.db_connector)

    def retrieve_shop_resource(self, shop_id: int):
        ''' Retrieves the underlying database information for the Shop and return a Shop Resource object '''
        try:
            shop = self.interface_shop.select_one(shop_id)
            _, name = shop
            return Shop.from_db(shop_id, name)

        except Exception as err:
            raise Exception(f'ERROR - Could not retrieve Shop from database: {err}')

    def persist_offline_availability_to_shop(self, shop_id, month, budget_amount) -> None:
        ''' Sets shops to offline persisting their state into the database '''
        self.interface_availability.persist_offline_availability(shop_id, month, budget_amount)
