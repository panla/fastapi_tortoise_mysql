class StatusCode(object):
    success = 10000

    http_error = 10400
    token_expired = 10401
    forbidden = 10403
    no_found = 100404
    validator_error = 10422

    server_error = 10500
    unknown_error = 10500


# 不要和自定义的异常冲突，会覆盖自定义抛出的异常
# 比如，已经自己抛出了 404，就不要在这里定义 404

middleware_codes = {
    405: {'status_code': 10405, 'message': 'Method Not Allowed', 'data': None},
    413: {'status_code': 10413, 'message': 'REQUEST_ENTITY_TOO_LARGE', 'data': None}
}
