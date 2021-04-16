"""定义错误码"""


class Code(object):
    success = 10000
    server_error = 10001
    unknown_error = 10002
    validator_error = 10003
    http_error = 10004

    no_exists = 10005
    token_expired = 10006


class CodeInfo(object):
    success = {'code': 10000, 'message': '请求成功'}
    token_expired = {'code': 10006, 'message': '请重新登录', 'data': None}
