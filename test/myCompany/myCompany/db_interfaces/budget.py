from myCompany.db_interfaces.common import BaseDBInterface


class BudgetDBInterface(BaseDBInterface):
    TABLE_NAME = 't_budgets'

    def __init__(self, db_connector) -> None:
        super().__init__(db_connector, self.TABLE_NAME)

    def select_one(self, shop_id):
        ''' Select one database entry from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT *
                           FROM {self.table_name}
                           WHERE a_shop_id = {shop_id}''')

        budget = cursor.fetchone()
        cursor.close()

        return budget

    def select_all_current_online_budgets(self, batch_date):
        ''' Return database Budget entries whose availability is online for the current month
            And for the current budget_amount
        '''
        query_date = batch_date.replace(day=1).strftime('%Y-%m-%d')
        cursor = self.db_connector.cursor()

        cursor.execute(f'''SELECT *
                           FROM {self.table_name} AS bg
                           WHERE NOT EXISTS (
                            SELECT *
                            FROM t_shops_offline_availability AS off
                            WHERE bg.a_shop_id = off.a_shop_id
                            AND bg.a_month = off.a_month
                            AND bg.a_budget_amount = off.a_budget_amount
                           )
                           AND bg.a_month = "{query_date}"
                        ''')

        budgets = (bg for bg in cursor.fetchall())
        cursor.close()

        return budgets
