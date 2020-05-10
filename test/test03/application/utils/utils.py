import application.enums.enums as enums


# Story 1
def generate_md5_hash_from_string(data=''):
    ''' Receives a string and return a hexadecimal md5 hash equivalent '''
    import hashlib

    custom_str = (data.values()[0] if
                  isinstance(data, dict) else
                  data)
    assert isinstance(custom_str, str), f'You must pass in a string type argument, got {type(custom_str)}'
    return hashlib.md5(custom_str.encode()).hexdigest()


# Story 2
def generate_uuid(custom_str):
    ''' Receives a source_strin and return a hexadecimal md5 hash equivalent given database prefix '''
    return generate_md5_hash_from_string(enums.DATABASE_UUID_PREFIX + custom_str)


# Story 2 and Story 3
def encrypt_password(password):
    ''' Uses core module bcrypt to ensure persistance of hash passwords in database '''
    from application.config.core import bcrypt

    return bcrypt.generate_password_hash(password)
