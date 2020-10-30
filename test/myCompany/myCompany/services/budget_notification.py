from collections import deque

from myCompany.db_interfaces.budget_notification import BudgetNotificationDBInterface, BudgetNotificationTypeDBInterface
from myCompany.resources.budget_notification import BudgetNotification
from myCompany.services.common import BaseService


class BudgetNotificationService(BaseService):
    def __init__(self, db_connector, batch_date) -> None:
        super().__init__(db_connector, batch_date)
        self._db_interface_notification = self._create_db_interface_notification()
        self._db_interface_type = self._create_db_interface_type()

    @property
    def budgets(self):
        ''' budgets getter method '''
        return self._budgets

    @property
    def db_interface_notification(self):
        ''' db_interface_notification getter method '''
        return self._db_interface_notification

    @property
    def db_interface_type(self):
        ''' db_interface_type getter method '''
        return self._db_interface_type

    def _create_db_interface_notification(self):
        ''' Creates a new BudgetNotificationDBInterface given the received db_connector '''
        return BudgetNotificationDBInterface(self.db_connector)

    def _create_db_interface_type(self):
        ''' Creates a new BudgetNotificationTypeDBInterface given the received db_connector '''
        return BudgetNotificationTypeDBInterface(self.db_connector)

    def _retrieve_notification_type_id(self, consumption_state):
        ''' Lookup on the Budget Notification Type table retrieving the match entry for the given consumption_state '''
        return self.db_interface_type.select_one_by_consumption_state(consumption_state)

    def _create_budget_notification(self, budget_resource, notification_type_id):
        ''' Creates a BudgetNotification Resource object with the Budget Notification Type db entry '''
        return BudgetNotification.from_type_db(budget_resource.shop,
                                               budget_resource.budget_amount,
                                               budget_resource.spent,
                                               budget_resource.month,
                                               self.batch_date,
                                               notification_type_id)

    def _has_preexisting_notification_to_budget(self, budget_resource, notification_type_id):
        return bool(self.db_interface_notification.select_one_by_notification_type(budget_resource.shop.shop_id,
                                                                                   budget_resource.month,
                                                                                   budget_resource.budget_amount,
                                                                                   notification_type_id))

    def _handle_budget_notifications(self, budget_resources):
        ''' Verifies budget eligibility to get notified and returns BudgetNotification Resource objects '''
        budget_notifications = deque()
        for bg in budget_resources:
            notification_type_id = self._retrieve_notification_type_id(bg.get_consumption_state())
            if notification_type_id and not self._has_preexisting_notification_to_budget(bg, notification_type_id):
                budget_notifications.append(self._create_budget_notification(bg, notification_type_id))

        return budget_notifications

    def _persist_new_notifications(self, budget_notification_resources):
        ''' Inserts multiple BudgetNotification Resource objects into underlying table '''
        self.db_interface_notification.insert_many(budget_notification_resources)

    def run_for_budgets(self, budget_resources):
        ''' Performs lookup, verification, creation and database persistence of Budget Notifications '''
        new_budget_notifications = self._handle_budget_notifications(budget_resources)
        try:
            self._persist_new_notifications(new_budget_notifications)
            return new_budget_notifications

        except Exception as err:
            raise Exception(f'ERROR: Could not persist budget notifications: {err}')
