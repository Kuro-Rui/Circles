class APIException(Exception):
    """Base class of all API exceptions."""


class InvalidKey(APIException):
    """Raised when the API key is invalid."""
    def __init__(self):
        super().__init__("Please provide a valid API key.")


class UserNotFound(APIException):
    """Raised when the specified user is not found."""
    def __init__(self):
        super().__init__("User not found.")
