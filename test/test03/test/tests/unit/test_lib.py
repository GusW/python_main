import application.lib.lib as lib


# Story 1
def test_generate_md5_hash_from_string():
    ("lib.generate_md5_hash_from_string should return a dictionary with a hexadecimal hash")

    # Given a random string
    random_string = 'user@newstore.com'

    # When I call generate_md5_hash_from_string
    result = lib.generate_md5_hash_from_string(random_string)

    # Then it should have returned a '6e7b920433c84d96e0ec3f45673fa390'
    result.should.equal('6e7b920433c84d96e0ec3f45673fa390')


# Story 2
def test_generate_uuid():
    ("lib.generate_uuid should return a hexadecimal hash")

    # Given a random string
    random_string = 'user@newstore.com'

    # When I call generate_md5_hash_from_string
    result = lib.generate_uuid(random_string)

    # Then it should have returned a '3169e2b24cdcd31bc71e8ad3dfea30e7'
    result.should.equal('3169e2b24cdcd31bc71e8ad3dfea30e7')


# Story 2 and Story 3
def test_encrypt_password():
    ("lib.encrypt_password should return an encrypted pass hash")

    # Given a random password
    random_password = 'notagoodpass'

    # When I call generate_md5_hash_from_string
    result = lib.encrypt_password(random_password)

    # Then it should have returned an encrypted hash
    result.should.be.a(bytes)
    result.shouldnt.equal(random_password)
