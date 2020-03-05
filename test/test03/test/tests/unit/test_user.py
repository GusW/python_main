from application.db_models.user import User
import application.enums.enums as enums
from tests.helpers import web_test


def test_create_user():
    ("user.__init__ should create a brand new user with custom UUID and password hash")

    # Given I have a valid data
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'

    # And that I call the User.__init__
    user = User(first_name, email, password)

    # Then it should be a User instance
    user.should.be.a(User)

    # And its UUID should be a string
    user.uuid.should.be.a(str)

    # And its password should be stored in bytes
    user.password.should.be.a(bytes)


def test_edit_user():
    ("user.edit_user should change the user attributes if modifications are passed in")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)
    uuid_before = user.uuid
    password_before = user.password

    # And that I call the edit_user with some valid modifications
    first_name_new = "Raymond"
    email_new = 'raymond@python.org'
    password_new = 'jupyter567'
    user.edit_user(first_name_new, email_new, password_new)
    password_after = user.password

    # Then its UUID should be the same as before
    user.uuid.should.be(uuid_before)

    # And its name should be the new name
    user.first_name.should.be(first_name_new)

    # And its email should be the new email
    user.email.should.be(email_new)

    # And its password shouldnt be the same as stored
    user.password.shouldnt.be(password_before)

    # However if I pass no changes to edit_user
    user.edit_user('', '', '')

    # Then its UUID should be the same as before
    user.uuid.should.be(uuid_before)

    # And its name should remain the new name
    user.first_name.should.be(first_name_new)

    # And its email should remain the new email
    user.email.should.be(email_new)

    # And its password remain as stored
    user.password.should.be(password_after)


def test_user_payload():
    ("user.payload should return a dict with user details")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)

    # And that I call the payload on the object
    result = user.payload()

    # Then the result should be a dict
    result.should.be.a(dict)

    # And the dict should have an expected structure
    result.should.equal({enums.FIRST_NAME_KEY: user.first_name,
                         enums.UUID_KEY: user.uuid,
                         enums.EMAIL_KEY: user.email})


@web_test
def test_get_all_instances(context):
    ("user.get_all_instances should return a list of users")

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

    # And that I call get_all_instances
    result = User.get_all_instances()

    # Then the result should be a list
    result.should.be.a(list)

    # And the users payload should be in the list
    user_created_1.should.be.within(result)
    user_created_2.should.be.within(result)


@web_test
def test_find_instance_by_email(context):
    ("user.find_instance_by_email should return a list of users with no element or a single one")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)
    user.persist()
    context.objects.append(user)

    # And that I call the find_instance_by_email with the user email
    result = User.find_instance_by_email(user.email)

    # Then the result should be a list
    result.should.be.a(list)

    # And the list should have an unique element
    len(result).should.equal(1)

    # And the user should be in the list
    user.should.be.within(result)

    # However if I call the find_instance_by_email with an invalid email
    result = User.find_instance_by_email("go@lang.org")

    # Then the result should be a list
    result.should.be.a(list)

    # And the list should be empty
    result.should.be.empty


@web_test
def test_find_instance_by_uuid(context):
    ("user.find_instance_by_uuid should return a list of users with no element or a single one")

    # Given I have an existing user
    first_name = 'Guido'
    email = 'guido@python.org'
    password = 'py123'
    user = User(first_name, email, password)
    user.persist()
    context.objects.append(user)

    # And that I call the find_instance_by_email with the user email
    result = User.find_instance_by_uuid(user.uuid)

    # Then the result should be a list
    result.should.be.a(list)

    # And the list should have an unique element
    len(result).should.equal(1)

    # And the user should be in the list
    user.should.be.within(result)

    # However if I call the find_instance_by_email with an invalid email
    result = User.find_instance_by_uuid("herecomesaninvalidUUID")

    # Then the result should be a list
    result.should.be.a(list)

    # And the list should be empty
    result.should.be.empty
