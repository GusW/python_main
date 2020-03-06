import application.db_interface.user_interface as user_interface
import application.enums.enums as enums
from application.db_models.user import User
from tests.helpers import web_test


# Story 2
@web_test
def test_create_database_user(context):
    ("user_interface.create_database_user should return an user payload (dict)")

    # Given I have a valid data
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    json_data = {enums.FIRST_NAME_KEY: first_name,
                 enums.EMAIL_KEY: email,
                 enums.PASSWORD_KEY: password}

    # And that I call create_database_user
    result = user_interface.create_database_user(**json_data)
    user = User.find_instance_by_email(email)[0]
    context.objects.append(user)

    # When I check the result

    # Then it should be a dictionary
    result.should.be.a(dict)

    # And it should be the user payload
    result.should.equal(user.payload())

    # However if I try to add the same json_data when I call create_database_user it should throw an Exception
    user_interface.create_database_user.when.called_with(**json_data).should.have.raised(Exception)

    # And if I try to add a json with missing information it should also throw an Exception
    json_data_invalid = {}
    user_interface.create_database_user.when.called_with(**json_data_invalid).should.have.raised(Exception)


# Story 3
@web_test
def test_edit_database_user(context):
    ("user_interface.edit_database_user should return an user payload (dict)")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)
    user.persist()
    context.objects.append(user)

    # And a valid json_data
    email_new = 'guido.van.rossum@python.org'
    password_new = 'ch4ngeMeL4terPleas3'
    json_data = {enums.UUID_KEY: user.uuid,
                 enums.EMAIL_KEY: email_new,
                 enums.PASSWORD_KEY: password_new}

    # And that I call edit_database_user
    result = user_interface.edit_database_user(**json_data)

    # When I check the result

    # Then it should be a dictionary
    result.should.be.a(dict)

    # And it should be the user payload
    result.should.equal(user.payload())

    # However if I try to edit the user email to another that exists in the database and call edit_database_user it should throw an Exception
    first_name_2 = 'Guido2'
    email_2 = 'guido2@python.org'
    password_2 = 'py123'
    user_2 = User(first_name_2, email_2, password_2)
    user_2.persist()
    context.objects.append(user_2)
    json_data_invalid = {enums.UUID_KEY: user.uuid,
                         enums.EMAIL_KEY: password_2}

    user_interface.create_database_user.when.called_with(**json_data_invalid).should.have.raised(Exception)

    # And if I dont a json with missing information it should also throw an Exception
    json_data_invalid_info = {enums.UUID_KEY: user.uuid}
    user_interface.create_database_user.when.called_with(**json_data_invalid_info).should.have.raised(Exception)

    # Or if I pass an inexisting UUID it should also throw an Exception
    json_data_invalid_uuid = {enums.UUID_KEY: 'someOddUUID'}
    user_interface.create_database_user.when.called_with(**json_data_invalid_uuid).should.have.raised(Exception)


# Story 4
@web_test
def test_get_database_user(context):
    ("user_interface.get_database_user should return an user payload (dict)")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)
    user.persist()
    context.objects.append(user)

    # And a valid json_data
    json_data = {enums.UUID_KEY: user.uuid}

    # And that I call get_database_user with its UUID
    result = user_interface.get_database_user(**json_data)

    # Then it should be a dictionary
    result.should.be.a(dict)

    # And it should be the user payload
    result.should.equal(user.payload())

    # However if I try to get an unknown UUID call edit_database_user it should throw an Exception
    json_data_invalid = {enums.UUID_KEY: 'someOddUUID'}
    user_interface.create_database_user.when.called_with(**json_data_invalid).should.have.raised(Exception)


# Story 5
@web_test
def test_get_database_users(context):
    ("user_interface.get_database_users should return a list of users payload (dict)")

    # Given I have existing users
    first_name_1 = 'Guido'
    email_1 = 'guido@python.org'
    password_1 = 'py123'
    user_created_1 = User(first_name_1, email_1, password_1)
    user_created_1.persist()
    context.objects.append(user_created_1)

    first_name_2 = 'Raymond'
    email_2 = 'raymond@python.org'
    password_2 = 'py567'
    user_created_2 = User(first_name_2, email_2, password_2)
    user_created_2.persist()
    context.objects.append(user_created_2)

    # And that I call get_database_users
    result = user_interface.get_database_users(**{})

    # Then it should be a list
    result.should.be.a(list)

    # And it should contains the users payload
    result.should.contain(user_created_1.payload())
    result.should.contain(user_created_2.payload())


# Story 6
@web_test
def test_delete_database_user(context):
    ("user_interface.delete_database_user should return an user payload (dict)")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user_created = User(first_name, email, password)
    user_created.persist()
    user_payload = user_created.payload()

    # And that I call delete_database_user with its email
    data_json = {enums.EMAIL_KEY: email}
    result = user_interface.delete_database_user(**data_json)

    # Then it should be a dictionary
    result.should.be.a(dict)

    # And it should be the user payload
    result.should.equal(user_payload)

    # However if I try to remove an unknown email and call delete_database_user it should throw an Exception
    json_data_invalid = {enums.EMAIL_KEY: 'some@oddemail.net'}
    user_interface.delete_database_user.when.called_with(**json_data_invalid).should.have.raised(Exception)
