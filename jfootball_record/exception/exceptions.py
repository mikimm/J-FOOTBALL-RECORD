
class AppException(Exception):
    pass


class NotFoundError(AppException):
    pass


class ExternalAPIError(AppException):
    pass