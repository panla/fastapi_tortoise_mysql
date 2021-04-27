"""定义错误码"""


class Code(object):
    success = 10000

    http_error = 10400
    token_expired = 10401
    forbidden = 10403
    no_found = 100404
    validator_error = 10422

    server_error = 10500
    unknown_error = 10500


class CodeInfo(object):
    success = {'code': Code.success, 'message': '请求成功'}
    token_expired = {'code': Code.token_expired, 'message': '请重新登录'}
