import application.enums.enums as enums
from application.config.core import db
from application.db_models.common import DatabaseMixin
import application.lib.lib as lib


class User(db.Model, DatabaseMixin):
    __tablename__ = 'user'

    first_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    uuid = db.Column(db.String, name="uuid", nullable=False)

    def __init__(self, first_name, email, password):
        self.first_name = first_name
        self.email = email
        self.password = self._encrypt_password(password)
        self.uuid = lib.generate_uuid(email)

    def __repr__(self):
        return f'<User {self.first_name}>'

    def edit_user(self, first_name, email, password):
        self.first_name = first_name or self.first_name
        self.email = email or self.email
        self.password = self._encrypt_password(password) if password else self.password

    def payload(self):
        return {enums.FIRST_NAME_KEY: self.first_name,
                enums.UUID_KEY: self.uuid,
                enums.EMAIL_KEY: self.email}

    @staticmethod
    def _encrypt_password(password):
        return lib.encrypt_password(password)

    @staticmethod
    def get_all_instances():
        return User.query.all()

    @staticmethod
    def find_instance_by_email(email):
        return User.query.filter_by(email=email).all()

    @staticmethod
    def find_instance_by_uuid(uuid):
        return User.query.filter_by(uuid=uuid).all()
