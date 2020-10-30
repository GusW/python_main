from collections import deque

from myCompany.db_interfaces.budget import BudgetDBInterface
from myCompany.resources.budget import Budget
from myCompany.services.common import BaseService
from myCompany.services.shop import ShopService


class BudgetService(BaseService):
    def __init__(self, db_connector, batch_date) -> None:
        super().__init__(db_connector, batch_date)
        self._db_interface = self._create_new_interface()

    @property
    def db_interface(self):
        ''' db_interface getter method '''
        return self._db_interface

    def _create_new_interface(self):
        ''' Creates a new BudgetDBInterface given the received db_connector '''
        return BudgetDBInterface(self.db_connector)

    def _retrieve_shop_resource(self, shop_id):
        ''' Retrieves the underlying database information for the Shop and return a Shop Resource object '''
        return ShopService(self.db_connector, self.batch_date).retrieve_shop_resource(shop_id)

    def retrieve_budget_resources(self) -> deque:
        ''' Retrieves the underlying database information for the Budgets and return Budget Resource objects '''
        try:
            budget_resources = deque()
            budgets = self.db_interface.select_all_current_online_budgets(self.batch_date)
            for budget_details in budgets:
                shop_id, month, amount, spent = budget_details
                shop_resource = self._retrieve_shop_resource(shop_id)
                budget_resources.append(Budget.from_db(shop_resource,
                                                       month,
                                                       amount,
                                                       spent))
            return budget_resources

        except Exception as err:
            raise Exception(f'ERROR - Could not retrieve Budgets from database: {err}')
