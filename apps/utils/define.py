class StatusCode(object):
    success = 10000

    bad_request = 40000
    unauthorized = 40001
    forbidden = 40003
    not_found = 40004
    method_not_allowed = 40005

    entity_too_large = 40013
    validator_error = 40422

    server_error = 40500
    unknown_error = 40500


# 不要和自定义的异常冲突，会覆盖自定义抛出的异常
# 比如，已经自己抛出了 404，就不要在这里定义 404

middleware_codes = {
    405: {'status_code': StatusCode.method_not_allowed, 'message': 'Method Not Allowed', 'data': None},
    413: {'status_code': StatusCode.entity_too_large, 'message': 'REQUEST_ENTITY_TOO_LARGE', 'data': None}
}
