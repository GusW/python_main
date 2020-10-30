from enum import Enum


class BudgetNotificationTypes(str, Enum):
    HALF_CONSUMED = 'spent half of your budget'
    FULLY_CONSUMED = 'spent your full budget'


# TODO Need to rethink how new insertions on database layer could be dinamically caught instead
map_db_budget_notification_types = {
    1: BudgetNotificationTypes.HALF_CONSUMED,
    2: BudgetNotificationTypes.FULLY_CONSUMED,
}


class BudgetNotification():
    def __init__(self,
                 shop,
                 budget_amount,
                 amount_spent,
                 month,
                 date,
                 notification_type: BudgetNotificationTypes) -> None:
        self._shop = shop
        self._budget_amount = budget_amount
        self._amount_spent = amount_spent
        self._month = month
        self._date = date
        self._notification_type = notification_type

    @classmethod
    def from_type_db(cls,
                     shop_resource,
                     budget_amount,
                     amount_spent,
                     month,
                     date,
                     notification_type_id: int) -> None:
        ''' Creates new BudgetNotification instance given the received database info '''
        return cls(shop_resource,
                   budget_amount,
                   amount_spent,
                   month,
                   date,
                   map_db_budget_notification_types.get(notification_type_id))

    @property
    def shop(self):
        ''' shop getter method '''
        return self._shop

    @property
    def budget_amount(self):
        ''' budget_amount getter method '''
        return self._budget_amount

    @property
    def amount_spent(self):
        ''' amount_spent getter method '''
        return self._amount_spent

    @property
    def month(self):
        ''' date getter method '''
        return self._month

    @property
    def date(self):
        ''' date getter method '''
        return self._date

    @property
    def notification_type(self) -> BudgetNotificationTypes:
        ''' notification_type getter method '''
        return self._notification_type

    def budget_is_fully_consumed(self) -> bool:
        ''' Helper method returns True if notification_type is FULLY_CONSUMED '''
        return self.notification_type == BudgetNotificationTypes.FULLY_CONSUMED

    def to_db(self) -> tuple:
        ''' Parses object information into plain database datatypes and returns a tuple with required database values'''
        return (self.shop.shop_id,
                self.month.strftime('%Y-%m-%d'),
                self.budget_amount,
                [k for k, v in map_db_budget_notification_types.items() if v == self.notification_type][0],
                self._create_notification_message(),
                self.date.strftime('%Y-%m-%d'))

    def _create_notification_message(self) -> str:
        ''' Responsible to build up the final notification message '''
        appendix_exp = ('Please notice we will make your listings unavailable until the next budget cycle' if
                        self.notification_type == BudgetNotificationTypes.FULLY_CONSUMED
                        else 'You may keep track of your current budget consumption in your shop dashboard')

        date_str = self.date.strftime('%d-%b-%Y')
        month_str = self.month.strftime('%b-%Y')
        consumption_percentage = '{0:.2f}'.format(100*(self.amount_spent / self.budget_amount))
        return f'Hi {self.shop.name} (ID {self.shop.shop_id}),\n \
                 Our last bugdet consolidation in {date_str} reports you have {self.notification_type.value}\n \
                 for the overall lenght/cumulative period of {month_str}:\n \
                 ==========================\n \
                 Consumption = {self.amount_spent}\n \
                 Monthly Budget = {self.budget_amount}\n \
                 Percentage = {consumption_percentage}%\n \
                 ==========================\n \
                 {appendix_exp}.\n \
                 Sincerily yours,\n \
                 myCompany - made for you\n'

    def send_notification(self) -> None:
        ''' Retrieves the notification message and sends to the shops using current notification service'''
        notification_service = print  # TODO create other service to send_email, send_whatsapp, send_sms, send_*
        return notification_service(self._create_notification_message())
