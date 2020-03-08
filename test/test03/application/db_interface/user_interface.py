import application.enums.enums as enums
from application.db_models.user import User


# Story 2
def create_database_user(**kwargs):
    ''' Interface to create user database entry
        Should receive first_name, email and password
        Will return first_name, email and uuid upon success
    '''
    email = kwargs.get(enums.EMAIL_KEY)
    if User.find_instance_by_email(email):
        raise Exception(f'Could not create user: email {email} already in use')

    first_name = kwargs.get(enums.FIRST_NAME_KEY)
    password = kwargs.get(enums.PASSWORD_KEY)
    try:
        new_user = User(first_name, email, password)
        new_user.persist()
        return new_user.payload()
    except Exception as err:
        raise Exception(f'Could not create user: {err}')


# Story 3
def edit_database_user(**kwargs):
    ''' Interface to edit user database entry
        Should receive UUID and first_name and/or email and/or password
        Will return first_name, email and uuid upon success
    '''
    user_list = User.find_instance_by_uuid(kwargs.get(enums.UUID_KEY))
    if user_list:
        user = user_list[0]
        first_name = kwargs.get(enums.FIRST_NAME_KEY)
        email = kwargs.get(enums.EMAIL_KEY)
        if email and User.find_instance_by_email(email):
            raise Exception(f'Could not edit user: {email} already in use')

        password = kwargs.get(enums.PASSWORD_KEY)
        if any([first_name, email, password]):
            try:
                user.edit_user(first_name, email, password)
                user.persist()
                return user.payload()
            except Exception as err:
                raise Exception(f'Could not edit user: {err}')

        else:
            raise Exception('No new user information was passed in')

    else:
        raise Exception('No user was found for the given UUID')


# Story 4
def get_database_user(**kwargs):
    ''' Interface to get user database entry
        Should receive UUID
    '''
    uuid = kwargs.get(enums.UUID_KEY)
    user_list = User.find_instance_by_uuid(uuid)
    if user_list:
        user = user_list[0]
        return user.payload()

    else:
        raise Exception(f'No user was found for the passed in UUID {uuid}')


# Story 5
def get_database_users(**kwargs):
    ''' Interface to get user database entries
    '''
    user_list = User.get_all_instances()
    if user_list:
        return [user.payload() for user in user_list]

    else:
        raise Exception('No user found in the database')


# Story 6
def delete_database_user(**kwargs):
    ''' Interface to remove user database entry
        Should receive email
    '''
    email = kwargs.get(enums.EMAIL_KEY)
    user_list = User.find_instance_by_email(email)
    if user_list:
        user = user_list[0]
        payload = user.payload()
        user.remove()
        return payload

    else:
        raise Exception(f'No user was found for the given email {email}')
