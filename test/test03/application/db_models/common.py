from application.config.core import db


class DatabaseMixin(object):

    def persist(self):
        ''' Recipe to persist database entries '''
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
