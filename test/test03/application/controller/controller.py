import application.db_interface.user_interface as user_interface
import application.enums.enums as enums
import application.utils.utils as utils
import application.utils.common as common


# Common
def _api_endpoint_dispatcher(function_handler, data=None):
    ''' Default dispatcher to endpoint requests
        Should call the passed function with the underlying request data
    '''
    payload, response_code = function_handler(data)
    return common.json_response(payload, response_code)


# Common
def _data_handler(function, data, required_keys=()):
    ''' Receives a JSON and returns the underlying function result'''
    assert isinstance(data, dict), f'No JSON dictionary - received a type {type(data)}'
    for key in required_keys:
        assert key in data, f'Got JSON dictionary with no required key: {data}'

    return function(**data)


# Common
def _data_error_handler(function, err):
    ''' Standard error handler will return a tuple containing
        A dict with the error message and a 500 HTTP status code
    '''
    formatted_function_name = ' '.join(function.__name__.split('_'))
    return ({enums.ERROR_KEY: f'Exception in {formatted_function_name} - {err}'},
            enums.HTTP_ERR_INT)


# Legacy
def _my_backend_function(data=None):
    try:
        payload = {"hello": "world"}
        return payload, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler("my backend function", err)


# Story 1
def _calculate_md5_handler(data):
    ''' Default handler to calculate md5 requests
        Receives JSON data and returns a tuple
        If successful, the tuple contains a dict {'md5': hash} and a int 200
        Will return a dict {'error': error_message} and a int 500 otherwise
    '''
    function_call = utils.generate_md5_hash_from_string
    try:
        payload_value = _data_handler(function_call,
                                      data,
                                      required_keys=(enums.DATA_KEY,))
        return {enums.MD5_KEY: payload_value}, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler(function_call, err)


# Story 2
def _create_user_handler(data):
    ''' Default handler to create and persist new user requests
        Receives JSON data and returns a tuple
        If successful, the tuple contains a dict with the underlying user info and a int 200
        Will return a dict {'error': error_message} and a int 500 otherwise
    '''
    function_call = user_interface.create_database_user
    try:
        payload_value = _data_handler(function_call,
                                      data,
                                      required_keys=(enums.FIRST_NAME_KEY,
                                                     enums.EMAIL_KEY,
                                                     enums.PASSWORD_KEY))
        return payload_value, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler(function_call, err)


# Story 3
def _edit_user_handler(data):
    ''' Default handler to edit user requests
        Receives JSON data and returns a tuple
        If successful, the tuple contains a dict with the underlying user info and a int 200
        Will return a dict {'error': error_message} and a int 500 otherwise
    '''
    function_call = user_interface.edit_database_user
    try:
        payload_value = _data_handler(function_call,
                                      data,
                                      required_keys=(enums.UUID_KEY,))
        return payload_value, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler(function_call, err)


# Story 4
def _get_user_handler(data):
    ''' Default handler to get user requests
        Receives JSON data and returns a tuple
        If successful, the tuple contains a dict with the underlying user info and a int 200
        Will return a dict {'error': error_message} and a int 500 otherwise
    '''
    function_call = user_interface.get_database_user
    try:
        payload_value = _data_handler(function_call,
                                      data,
                                      required_keys=(enums.UUID_KEY,))
        return payload_value, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler(function_call, err)


# Story 5
def _get_users_handler(data):
    ''' Default handler to get users requests
        Receives JSON data and returns a tuple
        If successful, the tuple contains a list of dicts with the underlying users info and a int 200
        Will return a dict {'error': error_message} and a int 500 otherwise
    '''
    function_call = user_interface.get_database_users
    try:
        payload_value = _data_handler(function_call,
                                      data)
        return payload_value, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler(function_call, err)


# Story 6
def _delete_user_handler(data):
    ''' Default handler to delete user requests
        Receives JSON data and returns a tuple
        If successful, the tuple contains a dicts with the underlying removed user info and a int 200
        Will return a dict {'error': error_message} and a int 500 otherwise
    '''
    function_call = user_interface.delete_database_user
    try:
        payload_value = _data_handler(function_call,
                                      data,
                                      required_keys=(enums.EMAIL_KEY,))
        return payload_value, enums.HTTP_SUCCESS
    except Exception as err:
        return _data_error_handler(function_call, err)


# Legacy
def api_example_route_get_controller():
    return _api_endpoint_dispatcher(_my_backend_function)


# Story 1
def api_calculate_md5_controller(data):
    ''' Triggers the dispatcher with the _calculate_md5_handler and the received data '''
    return _api_endpoint_dispatcher(_calculate_md5_handler, data)


# Story 2
def api_create_user_controller(data):
    ''' Triggers the dispatcher with the _create_user_handler and the received data '''
    return _api_endpoint_dispatcher(_create_user_handler, data)


# Story 3
def api_edit_user_controller(uuid, data):
    ''' Triggers the dispatcher with the _edit_user_handler and the received data and uuid '''
    data[enums.UUID_KEY] = uuid
    return _api_endpoint_dispatcher(_edit_user_handler, data)


# Story 4
def api_get_user_controller(uuid):
    ''' Triggers the dispatcher with the _get_user_handler and the received uuid '''
    data = {enums.UUID_KEY: uuid}
    return _api_endpoint_dispatcher(_get_user_handler, data)


# Story 5
def api_get_users_controller():
    ''' Triggers the dispatcher with the _get_users_handler '''
    return _api_endpoint_dispatcher(_get_users_handler, {})


# Story 6
def api_delete_user_controller(email):
    ''' Triggers the dispatcher with the _delete_user_handler and the received email '''
    data = {enums.EMAIL_KEY: email}
    return _api_endpoint_dispatcher(_delete_user_handler, data)
