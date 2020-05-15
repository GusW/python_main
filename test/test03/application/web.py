from flask import render_template, request

import application.config.core as core
import application.controller.controller as controller
import application.enums.enums as enums

application = core.application


@application.route("/", methods=[enums.HTTP_REQ_GET])
def frontend():
    return render_template("index.html")


@application.route("/api/example", methods=[enums.HTTP_REQ_GET])
def api_example_route_get():
    return controller.api_example_route_get_controller()

# Story 1
@application.route("/api/calculate-md5", methods=[enums.HTTP_REQ_POST])
def api_calculate_md5():
    ''' Entry point of requests to calculate md5 hash
        Should return a JSON response with an underlying data and a status code
    '''
    return controller.api_calculate_md5_controller(request.json)

# Story 2
@application.route("/api/user", methods=[enums.HTTP_REQ_POST])
def api_create_user():
    ''' Entry point of requests to create a new user
        Should return a JSON response with an underlying data and a status code
    '''
    return controller.api_create_user_controller(request.json)

# Story 3 and 4
@application.route("/api/user/<string:uuid>", methods=[enums.HTTP_REQ_GET,
                                                       enums.HTTP_REQ_POST])
def api_get_or_edit_user(uuid):
    ''' Entry point of requests to edit or get existing users
        Should return a JSON response with an underlying data and a status code
    '''
    if request.method == enums.HTTP_REQ_GET:
        return controller.api_get_user_controller(uuid)

    return controller.api_edit_user_controller(uuid, request.json)

# Story 5
@application.route("/api/users", methods=[enums.HTTP_REQ_GET])
def api_get_users():
    ''' Entry point of requests to retrieve all database users
        Should return a JSON response with an underlying data and a status code
    '''
    return controller.api_get_users_controller()


# Story 6
@application.route("/api/user/<string:email>", methods=[enums.HTTP_REQ_DELETE])
def api_delete_user(email):
    ''' Entry point of requests to retrieve all database users
        Should return a JSON response with an underlying data and a status code
    '''
    return controller.api_delete_user_controller(email)


if __name__ == "__main__":
    from application.config.db_config import DBConfig

    DBConfig().handle_existing_database()
    application.run(
        # TODO pass in OS ENV
        # host='0.0.0.0',
        # port=5000
    )
