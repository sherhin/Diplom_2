class Endpoints:
    BASE = 'https://stellarburgers.nomoreparties.site/'
    AUTHORIZATION = 'api/auth/login'
    LOGOUT = 'api/auth/logout'
    TOKEN = 'api/auth/token'
    USER = 'api/auth/user'
    ORDERS = 'api/orders'
    ALL_ORDERS = 'api/orders/all'
    PASSWORD_RESET = 'api/password-reset'
    REGISTER = 'api/auth/register'
    ORDER_HISTORY = 'api/order-history'

class HttpMethods:
    get = 'GET'
    post = 'POST'
    patch = 'PATCH'
    delete = 'DELETE'


class ResponseTexts:
    user_created_code = 200
    user_exists = [403, '{"success":false,"message":"User already exists"}']
    user_without_required_fields = [403, '{"success":false,"message":"Email, password and name are required fields"}']
    user_authorizated_code = 200
    user_bad_authorization = [401, '{"success":false,"message":"email or password are incorrect"}']
    order_without_ingredients = [400, '{"success":false,"message":"Ingredient ids must be provided"}']
    incorrect_hash_code = 500
    get_order_non_authorize = [401, '{"success":false,"message":"You should be authorised"}']
    change_user_data_non_authorize = [401, '{"success":false,"message":"You should be authorised"}']