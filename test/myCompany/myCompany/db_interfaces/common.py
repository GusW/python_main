
class BaseDBInterface():
    def __init__(self, db_connector, table_name) -> None:
        self._db_connector = db_connector
        self._table_name = table_name

    @property
    def db_connector(self):
        ''' db_connector getter method '''
        return self._db_connector

    @property
    def table_name(self):
        ''' table_name getter method '''
        return self._table_name

    def select_all(self):
        ''' Select all database entries from table '''
        cursor = self.db_connector.cursor()
        cursor.execute(f'''SELECT *
                           FROM {self.table_name}''')

        items = (item for item in cursor.fetchall())

        cursor.close()

        return items
