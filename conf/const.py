class StatusCode(object):
    Success = 10000

    BadRequest = 40000
    Unauthorized = 40100
    Forbidden = 40300
    NotFound = 40400
    MethodNotAllowed = 40500
    NotAcceptable = 40600
    RequestTimeout = 40800
    LengthRequired = 41100
    EntityTooLarge = 41300
    RequestUriTooLong = 41400
    ValidatorError = 42200
    RequestValidatorError = 42201
    AssertValidatorError = 42202
    Locked = 42300
    HeaderFieldsTooLarge = 43100

    ServerError = 45000
    UnknownError = 45001


class PaginateConst:
    DefaultNum = 1
    DefaultSize = 10

    MinNum = 1
    MaxSize = 40


class EnvConst:

    TEST = 'test'
    PRD = 'prd'
    DEV = 'dev'
