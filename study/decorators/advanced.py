def requires_permission(sPermission):
    def decorator(fn):
        def decorated(*args, **kwargs):
            lPermissions = get_permissions(current_user_id())
            if sPermission in lPermissions:
                return fn(*args, **kwargs)

            raise Exception("permission denied")

        return decorated

    return decorator


def get_permissions(iUserId):  # this is here so that the decorator doesn't throw NameErrors
    return ['logged_in', 'premium_member']


def current_user_id():  # ditto on the NameErrors
    return 1

# and now we can decorate stuff...
@requires_permission('administrator')
def delete_user(iUserId):
    """
    delete the user with the given Id. This function is only accessible to users with administrator permissions
    """
    pass


@requires_permission('logged_in')
def new_game():
    """
    any logged in user can start a new game
    """
    pass


@requires_permission('premium_member')
def premium_checkpoint():
    """
    save the game progress, only accessable to premium members
    """
    pass


def outer_decorator(*outer_args, **outer_kwargs):
    def decorator(fn):
        def decorated(*args, **kwargs):
            lambda x: x(*outer_args, **outer_kwargs)
            return fn(*args, **kwargs)
        return decorated
    return decorator
