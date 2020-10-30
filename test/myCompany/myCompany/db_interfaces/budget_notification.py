from myCompany.db_interfaces.common import BaseDBInterface


class BudgetNotificationTypeDBInterface(BaseDBInterface):
    def __init__(self, db_connector) -> None:
        super().__init__(db_connector, 't_budget_notification_types')

    def select_one(self, type_id):
        ''' Select one database entry from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT *
                           FROM {self.table_name}
                           WHERE a_id = {type_id}''')

        budget = cursor.fetchone()
        cursor.close()

        return budget

    def select_one_by_consumption_state(self, consumption_state):
        ''' Select one database entry from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT a_id
                           FROM {self.table_name}
                           WHERE a_target BETWEEN 0 AND {consumption_state}
                           ORDER BY a_target DESC
                           LIMIT 1''')

        budget = cursor.fetchone()
        cursor.close()

        return budget[0] if budget else None


class BudgetNotificationDBInterface(BaseDBInterface):
    def __init__(self, db_connector) -> None:
        super().__init__(db_connector, 't_budget_notifications')

    def select_one(self, shop_id):
        ''' Select one database entry from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT *
                           FROM {self.table_name}
                           WHERE a_shop_id = {shop_id}''')

        budget = cursor.fetchone()
        cursor.close()

        return budget

    def select_one_by_notification_type(self, shop_id, a_month, a_amount, a_type_id):
        ''' Select one database entry from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT *
                           FROM {self.table_name}
                           WHERE a_shop_id = {shop_id}
                           AND a_month = "{a_month.strftime('%Y-%m-%d')}"
                           AND a_amount = {a_amount}
                           AND a_type_id = {a_type_id}''')

        budget = cursor.fetchone()
        cursor.close()

        return budget

    def insert_many(self, budget_notification_resources):
        ''' Insert multiple database entries into table '''
        cursor = self.db_connector.cursor()
        sql = (f'''INSERT
                   INTO {self.table_name} (a_shop_id, a_month, a_amount, a_type_id, a_message, a_sent_in)
                   VALUES (%s, %s, %s, %s, %s, %s)''')

        values = [bg_nt.to_db() for bg_nt in budget_notification_resources]

        cursor.executemany(sql, values)
        self.db_connector.commit()

        return cursor.rowcount
