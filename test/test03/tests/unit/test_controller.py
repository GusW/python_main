import application.controller.controller as controller
import application.enums.enums as enums
from application.db_models.user import User
from tests.helpers import web_test


# Common
def test__api_endpoint_dispatcher():
    ("controller._api_endpoint_dispatcher should return a json reponse with a payload and a response code")

    # Given a mocked function
    def _mocked_function(random=""):
        return {'mocked': random}, enums.HTTP_SUCCESS

    # And a random dict
    random_dict = {'random': 'user@newstore.com'}

    # When I call _api_endpoint_dispatcher with the _mocked_function
    result = controller._data_handler(_mocked_function,
                                      random_dict,
                                      ('random',))

    # Then it should have returned the _mocked_function return
    result.should.equal(({'mocked': 'user@newstore.com'}, enums.HTTP_SUCCESS))


# Common
def test__data_handler():
    ("controller._data_handler should return the passed in function's return")

    # Given a mocked function
    def _mocked_function(random=""):
        return f'mocked {random}'

    # And a random dict
    random_dict = {'random': 'user@newstore.com'}

    # When I call _data_handler with the _mocked_function
    result = controller._data_handler(_mocked_function,
                                      random_dict,
                                      ('random',))

    # Then it should have returned the _mocked_function return
    result.should.equal('mocked user@newstore.com')


# Common
def test__data_error_handler():
    ("controller._data_error_handler should return a tuple with a dictionary and a 500 status code")

    # Given a mocked function
    def _mocked_function():
        pass

    # And a random error
    random_err = 'Boom! Bang!'

    # When I call _data_error_handler with the _mocked_function
    result = controller._data_error_handler(_mocked_function,
                                            random_err)

    # Then it should have returned the _mocked_function return
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict and a 500 status code
    payload_dict.should.have.key('error').should.contain(random_err)
    http_status_code.should.equal(500)


# Legacy
def test__my_backend_function():
    ("controller._my_backend_function should return a dictionary")

    # Given that I call _my_backend_function
    result = controller._my_backend_function(None)

    # When I check the result

    # Then it should be a tuple
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # HTTP status code should be 200
    http_status_code.should.equal(enums.HTTP_SUCCESS)

    # And the payload dict should be: hello: world
    payload_dict.should.equal({"hello": "world"})


# Story 1
def test__calculate_md5_handler():
    ("controller._calculate_md5_handler should return a tuple with a dictionary and a HTTP code status")

    # Given I have a valid json_data
    json_data = {enums.DATA_KEY: "user@newstore.com"}

    # And that I call calculate_md5_handler
    result = controller._calculate_md5_handler(json_data)

    # When I check the result

    # Then it should be a tuple
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict and a 200 status code
    payload_dict.should.have.key(enums.MD5_KEY).being.equal('6e7b920433c84d96e0ec3f45673fa390')
    http_status_code.should.equal(enums.HTTP_SUCCESS)

    # Given I have an invalid json_data
    json_data = {enums.DATA_KEY: 23}

    # And that I call _calculate_md5_handler
    result = controller._calculate_md5_handler(json_data)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict and a 200 status code
    payload_dict.should.have.key(enums.ERROR_KEY)
    http_status_code.should.equal(enums.HTTP_ERR_INT)


# Story 2
@web_test
def test__create_user_handler(context):
    ("controller._create_user_handler should return a tuple with a dictionary and a HTTP code status")

    # Given I have a valid json_data
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    json_data = {enums.FIRST_NAME_KEY: first_name,
                 enums.EMAIL_KEY: email,
                 enums.PASSWORD_KEY: password}

    # And that I call _create_user_handler
    result = controller._create_user_handler(json_data)
    user = User.find_instance_by_email(email)[0]
    context.objects.append(user)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict and a 200 status code
    payload_dict.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    payload_dict.should.have.key(enums.EMAIL_KEY).being.equal(email)
    payload_dict.should.have.key(enums.UUID_KEY).being.equal(user.uuid)

    http_status_code.should.equal(enums.HTTP_SUCCESS)

    # However if I try to add the same json_data when I call _create_user_handler
    result = controller._create_user_handler(json_data)

    # When I check the result

    # Then it should be a tuple
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict with an error and a 500 status code
    payload_dict.should.have.key('error').should.contain(email)
    http_status_code.should.equal(500)


# Story 3
@web_test
def test__edit_user_handler(context):
    ("controller._edit_user_handler should return a tuple with a dictionary and a HTTP code status")

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

    # And that I call _edit_user_handler
    result = controller._edit_user_handler(json_data)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict and a 200 status code
    payload_dict.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    payload_dict.should.have.key(enums.EMAIL_KEY).being.equal(email_new)
    payload_dict.should.have.key(enums.UUID_KEY).being.equal(user.uuid)
    http_status_code.should.equal(enums.HTTP_SUCCESS)

    # However if I call the _edit_user_handler and pass no changes
    json_data_invalid = {enums.UUID_KEY: user.uuid}
    result = controller._edit_user_handler(json_data_invalid)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict with an error and a 500 status code
    payload_dict.should.have.key('error').should.contain('No new user information')
    http_status_code.should.equal(enums.HTTP_ERR_INT)

# Story 4
@web_test
def test__get_user_handler(context):
    ("controller._get_user_handler should return a tuple with a dictionary and a HTTP code status")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)
    user.persist()
    context.objects.append(user)

    # And that I call _get_user_handler with an valid uuid
    uuid = user.uuid
    json_data = {enums.UUID_KEY: uuid}
    result = controller._get_user_handler(json_data)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict and a 200 status code
    payload_dict.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    payload_dict.should.have.key(enums.EMAIL_KEY).being.equal(email)
    payload_dict.should.have.key(enums.UUID_KEY).being.equal(uuid)
    http_status_code.should.equal(enums.HTTP_SUCCESS)

    # However if I call with an invalid uuid
    invalid_uuid = 'justsomedummystuff'
    json_data_invalid = {enums.UUID_KEY: invalid_uuid}
    result = controller._get_user_handler(json_data_invalid)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict with an error and a 500 status code
    payload_dict.should.have.key('error').should.contain(invalid_uuid)
    http_status_code.should.equal(enums.HTTP_ERR_INT)


# Story 5
@web_test
def test__get_users_handler(context):
    ("controller._get_users_handler should return a tuple with a list of dictionaries and a HTTP code status")

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

    # And that I call _get_users_handler
    result = controller._get_users_handler({})

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_list, http_status_code = result

    # And it should have a list of dicts and a 200 status code
    {enums.FIRST_NAME_KEY: first_name_1,
     enums.EMAIL_KEY: email_1,
     enums.UUID_KEY: user_created_1.uuid}.should.be.within(payload_list)

    {enums.FIRST_NAME_KEY: first_name_2,
     enums.EMAIL_KEY: email_2,
     enums.UUID_KEY: user_created_2.uuid}.should.be.within(payload_list)

    http_status_code.should.equal(enums.HTTP_SUCCESS)


# Story 6
@web_test
def test__delete_user_handler(context):
    ("controller._delete_user_handler should return a tuple with a dictionary and a HTTP code status")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user_created = User(first_name, email, password)
    user_created.persist()

    # And that I call _delete_user_handler
    data_json = {enums.EMAIL_KEY: email}
    result = controller._delete_user_handler(data_json)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a list of dicts and a 200 status code
    payload_dict.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    payload_dict.should.have.key(enums.EMAIL_KEY).being.equal(email)
    payload_dict.should.have.key(enums.UUID_KEY).being.equal(user_created.uuid)
    http_status_code.should.equal(enums.HTTP_SUCCESS)

    # And the user should not be persisted anymore
    user_list = User.find_instance_by_email(email)
    user_list.should.be.empty

    # However if I try to remove an inexisting email
    invalid_email = 'just@somedummy.stuff'

    # And that I call _delete_user_handler
    json_data_invalid = {enums.EMAIL_KEY: invalid_email}
    result = controller._delete_user_handler(json_data_invalid)

    # When I check the result

    # Then it should be a tuple containing a dict and an int
    result.should.be.a(tuple)
    payload_dict, http_status_code = result

    # And it should have a dict with an error and a 500 status code
    payload_dict.should.have.key('error').should.contain(invalid_email)
    http_status_code.should.equal(enums.HTTP_ERR_INT)
