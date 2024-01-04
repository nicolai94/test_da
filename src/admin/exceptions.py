from starlette import status

from src.exceptions import CustomException


class UserDoesNotExistsException(CustomException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Пользователь не найден"
        self.headers = None