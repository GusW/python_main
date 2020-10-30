
class BaseService():
    def __init__(self, db_connector, batch_date) -> None:
        self._db_connector = db_connector
        self._batch_date = batch_date

    @property
    def db_connector(self):
        ''' db_connector getter method '''
        return self._db_connector

    @property
    def batch_date(self):
        ''' batch_date getter method '''
        return self._batch_date
