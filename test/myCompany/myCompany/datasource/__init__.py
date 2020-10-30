import os

from myCompany.datasource.db_connector import get_database_connector

db = os.getenv("DB_NAME")
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

db_connector = get_database_connector(host=host,
                                      port=port,
                                      database=db,
                                      user=user,
                                      password=password)
