from myCompany.db_interfaces.common import BaseDBInterface


class ShopDBInterface(BaseDBInterface):
    def __init__(self, db_connector) -> None:
        super().__init__(db_connector, 't_shops')

    def select_one(self, shop_id):
        ''' Select one database entry from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT *
                           FROM {self.table_name}
                           WHERE a_id = {shop_id}''')

        shop = cursor.fetchone()

        cursor.close()
        return shop


class ShopOfflineAvailabilityDBInterface(BaseDBInterface):
    def __init__(self, db_connector) -> None:
        super().__init__(db_connector, 't_shops_offline_availability')

    def persist_offline_availability(self, shop_id, month, budget_amount):
        ''' Insert database entry into table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''INSERT
                           INTO {self.table_name} (a_shop_id, a_month, a_budget_amount)
                           VALUES ({shop_id}, "{month.strftime('%Y-%m-%d')}", {budget_amount})''')

        self.db_connector.commit()

        return cursor.rowcount
