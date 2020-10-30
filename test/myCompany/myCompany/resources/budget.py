class Budget():
    def __init__(self,
                 shop,
                 month,
                 budget_amount,
                 spent) -> None:
        self._shop = shop
        self._month = month
        self._budget_amount = budget_amount
        self._spent = spent

    @classmethod
    def from_db(cls, shop, month, budget_amount, spent) -> None:
        ''' Creates new Budget instance given the received database info '''
        return cls(shop, month, budget_amount, spent)

    @property
    def shop(self):
        ''' shop getter method '''
        return self._shop

    @property
    def month(self):
        ''' month getter method '''
        return self._month

    @property
    def budget_amount(self):
        ''' budget_amount getter method '''
        return self._budget_amount

    @property
    def spent(self):
        ''' spent getter method '''
        return self._spent

    def get_consumption_state(self):
        ''' Calculates de current percentual Budget consumption '''
        return 100 * (self.spent / self.budget_amount)
