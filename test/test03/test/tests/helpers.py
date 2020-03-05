from collections import deque

from application.config.core import db
from application.config.db_config import DBConfig
from application.web import application
from sure import scenario


def before_each_test(context):

    DBConfig().handle_existing_database()
    context.web = application
    context.http = context.web.test_client()
    context.session = db.session
    context.objects = deque()


def after_each_test(context):
    # certainly there is a more elegant way to do this
    # extensive documentation on db engine and sessionmaker
    # however it seems to require a major architecture refactor
    for obj in list(context.objects):
        context.session.delete(obj)

    context.session.commit()


web_test = scenario(before_each_test, after_each_test)
