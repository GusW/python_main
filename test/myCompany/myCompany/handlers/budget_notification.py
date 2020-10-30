from datetime import date

from myCompany.services.budget import BudgetService
from myCompany.services.budget_notification import BudgetNotificationService
from myCompany.services.shop import ShopService


class BudgetNotificationHandler():
    def __init__(self, db_connector, batch_date) -> None:
        self._db_connector = db_connector
        self._batch_date = batch_date

    @property
    def db_connector(self):
        ''' db_connector getter method '''
        return self._db_connector

    @property
    def batch_date(self) -> date:
        ''' batch_date getter method '''
        return self._batch_date

    def _get_current_online_budgets(self):
        ''' Retrieves the current online budgets if they require to be notified '''
        return BudgetService(self.db_connector, self.batch_date).retrieve_budget_resources()

    def _create_budget_notifications(self, budgets):
        ''' Creates budget notification resources '''
        return BudgetNotificationService(self.db_connector, self.batch_date).run_for_budgets(budgets)

    def _verify_pending_notifications(self):
        ''' Retrieves the current online budgets and handle the creation of notifications to these '''
        current_online_budgets = self._get_current_online_budgets()
        return self._create_budget_notifications(current_online_budgets)

    def _handle_shop_availability(self, budget_notification) -> None:
        ''' If the budget is FULLY_CONSUMED then the Shop must go offline '''
        ShopService(self.db_connector,
                    self.batch_date).persist_offline_availability_to_shop(budget_notification.shop.shop_id,
                                                                          budget_notification.month,
                                                                          budget_notification.budget_amount)

    def send_notifications_to_unnotified_budgets(self) -> None:
        ''' Verifies the need to create new budget notifications and triggers their notifications '''
        print(f'... Running budget notifications to target date {self.batch_date}')
        pending_notifications = self._verify_pending_notifications()
        if pending_notifications:
            for nt in pending_notifications:
                if nt.budget_is_fully_consumed():
                    self._handle_shop_availability(nt)

                nt.send_notification()
        else:
            print(f'>>> No unnotified budgets were found as of {self.batch_date}.')

        self.db_connector.close()
