"""Example login code"""
from crypt import crypt
import sqlite3
import pathlib


salt = '$6$ZmBkxkRFj03LQOvr'  # Bad security, store safely
db_name = "passwords.db"
db_path = f"{pathlib.Path(__file__).parent.resolve()}/{db_name}"


def user_passwd(user):
    """Get user password from db"""
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row  # Access columns by names

    cur = db.cursor()
    # pdb.set_trace()
    cur.execute('SELECT passwd FROM users WHERE user = ?', (user, ))
    row = cur.fetchone()
    db.close()
    if row is None:  # No such user
        raise KeyError(user)
    return row['passwd']


def encrypt_passwd(passwd):
    """Encrypt user password"""
    return crypt(passwd, salt)


def login(user, password):
    """Return True is user/password pair matches"""
    try:
        db_passwd = user_passwd(user)
    except KeyError:
        return False

    passwd = encrypt_passwd(password)
    return passwd == db_passwd
