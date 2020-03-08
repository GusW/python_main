import json

import application.enums.enums as enums
from application.db_models.user import User
from tests.helpers import web_test

# This test suite uses the python module "sure":
#
# https://sure.readthedocs.io/en/latest/api-reference.html#example-setup-a-flask-app-for-testing


# Legacy
@web_test
def test_index_page(context):
    ("GET on / should render an HTML page")

    # Given that I perform a GET /
    response = context.http.get("/")

    # Then check if the status was 200
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I check the content type is html
    response.headers.should.have.key("Content-Type")

    # Then it should be html
    response.headers["Content-Type"].should.contain("text/html")


# Legacy
@web_test
def test_hello_world(context):
    ("GET on /api/example should return a json containing hello world")

    # Given that I perform a GET /api/example
    response = context.http.get("/api/example")

    # When I check the response
    response.headers.should.have.key(
        "Content-Type").being.equal("application/json")

    # And check if the status was 200
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have the key "hello" with value "world"
    data.should.have.key("hello").being.equal("world")


# Story 1
@web_test
def test_api_calculate_md5(context):
    ("POST on /api/calculate-md5 should return a json containing the hexadigested hash from the string")

    # Given that I perform a POST to /api/calculate-md5 with a valid JSON data
    json_data = {'data': 'user@newstore.com'}
    response = context.http.post('/api/calculate-md5', json=json_data)

    # When I check the response
    response.headers.should.have.key(
        "Content-Type").being.equal("application/json")

    # And check if the status was success
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have a specific key and value as below
    data.should.have.key('md5').being.equal('6e7b920433c84d96e0ec3f45673fa390')


# Story 2
@web_test
def test_api_create_user(context):
    ("POST on /api/user should return a json containing the information persisted in database")

    # Given that I perform a POST to /api/user with a valid JSON data
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    json_data = {enums.FIRST_NAME_KEY: first_name,
                 enums.EMAIL_KEY: email,
                 enums.PASSWORD_KEY: password}

    response = context.http.post('/api/user', json=json_data)
    context.objects.append(User.find_instance_by_email(email)[0])

    # When I check the response
    response.headers.should.have.key("Content-Type").being.equal("application/json")

    # And check if the status was success
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have a specific key and value as below
    data.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    data.should.have.key(enums.EMAIL_KEY).being.equal(email)
    data.should.have.key(enums.UUID_KEY)


# Story 3
@web_test
def test_api_edit_user(context):
    ("POST on /api/user/<string:uuid> should edit the user persisted in database")

    # Given that I have already an user in the database
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user_created = User(first_name, email, password)
    user_created.persist()
    context.objects.append(user_created)

    # Given that I perform a POST to /api/user/uuid with a valid JSON data
    user_uuid = user_created.uuid
    new_email = "dummy@email.com"
    json_data = {enums.EMAIL_KEY: new_email}
    response = context.http.post(f'/api/user/{user_uuid}', json=json_data)

    # When I check the response
    response.headers.should.have.key("Content-Type").being.equal("application/json")

    # And check if the status was success
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have a specific key and value as below
    data.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    data.should.have.key(enums.EMAIL_KEY).being.equal(new_email)
    data.should.have.key(enums.UUID_KEY).being.equal(user_uuid)


# Story 4
@web_test
def test_api_get_user(context):
    ("GET on /api/user/<string:uuid> should get the user persisted in database")

    # Given that I have already an user in the database
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user_created = User(first_name, email, password)
    user_created.persist()
    context.objects.append(user_created)

    # Given that I perform a POST to /api/user/uuid with a valid JSON data
    user_uuid = user_created.uuid
    response = context.http.get(f'/api/user/{user_uuid}')

    # When I check the response
    response.headers.should.have.key("Content-Type").being.equal("application/json")

    # And check if the status was success
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have a specific key and value as below
    data.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    data.should.have.key(enums.EMAIL_KEY).being.equal(email)
    data.should.have.key(enums.UUID_KEY).being.equal(user_uuid)


# Story 5
@web_test
def test_api_get_users(context):
    ("GET on /api/users should get all the users persisted in database")

    # Given that I have already users in the database
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

    # And I perform a GET to /api/users
    response = context.http.get('/api/users')

    # When I check the response
    response.headers.should.have.key("Content-Type").being.equal("application/json")

    # And check if the status was success
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should be a list and have a specific key and value as below
    {enums.FIRST_NAME_KEY: first_name_1,
     enums.EMAIL_KEY: email_1,
     enums.UUID_KEY: user_created_1.uuid}.should.be.within(data)

    {enums.FIRST_NAME_KEY: first_name_2,
     enums.EMAIL_KEY: email_2,
     enums.UUID_KEY: user_created_2.uuid}.should.be.within(data)


# Story 6
@web_test
def test_api_delete_user(context):
    ("DELETE on /api/user/<string:email> should remove the user persisted in database")

    # Given that I have already an user in the database
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user_created = User(first_name, email, password)
    user_created.persist()

    # Given that I perform a DELETE to /api/user/email
    response = context.http.delete(f'/api/user/{email}')

    # When I check the response
    response.headers.should.have.key("Content-Type").being.equal("application/json")

    # And check if the status was success
    response.status_code.should.equal(enums.HTTP_SUCCESS)

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have a specific key and value as below
    data.should.have.key(enums.FIRST_NAME_KEY).being.equal(first_name)
    data.should.have.key(enums.EMAIL_KEY).being.equal(email)
    data.should.have.key(enums.UUID_KEY).being.equal(user_created.uuid)

    # And the user should not be persisted anymore
    user_list = User.find_instance_by_email(email)
    user_list.should.be.empty
