import mysql.connector


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class _DatabaseConnector(metaclass=Singleton):
    def __init__(self,
                 host: str = '0.0.0.0',
                 port: str = '3306',
                 database: str = '',
                 user: str = 'root',
                 password: str = 'password') -> None:
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password

    @property
    def host(self) -> str:
        ''' host getter method '''
        return self._host

    @property
    def port(self) -> str:
        ''' port getter method '''
        return self._port

    @property
    def database(self) -> str:
        ''' database getter method '''
        return self._database

    @property
    def user(self) -> str:
        ''' user getter method '''
        return self._user

    @property
    def password(self) -> str:
        ''' password getter method '''
        return self._password

    def crate_connection(self) -> mysql.connector:
        ''' Returns a Mysql DB Connection '''
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
        )


def get_database_connector(host: str = '0.0.0.0',
                           port: int = 3306,
                           database: str = '',
                           user: str = 'root',
                           password: str = 'password'):
    ''' Creates a singleton _DatabaseConnector and returns a Mysql DB Connection '''
    return _DatabaseConnector(host=host,
                              port=port,
                              database=database,
                              user=user,
                              password=password).crate_connection()
