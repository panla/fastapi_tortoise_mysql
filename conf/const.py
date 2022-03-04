class StatusCode(object):
    success = 10000

    bad_request = 40000
    unauthorized = 40100
    forbidden = 40300
    not_found = 40400
    method_not_allowed = 40500
    not_acceptable = 40600
    request_timeout = 40800
    length_required = 41100
    entity_too_large = 41300
    request_uri_too_long = 41400
    validator_error = 42200
    locked = 42300
    header_fields_too_large = 43100

    server_error = 45000
    unknown_error = 45001


class PaginateConst:
    DefaultNum = 1
    DefaultSize = 10

    MinNum = 1
    MaxSize = 40


class EnvConst:

    TEST = 'test'
    PRD = 'prd'
    DEV = 'dev'
