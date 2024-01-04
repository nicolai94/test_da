from fastapi import HTTPException


class CustomException(HTTPException):
    def __init__(self, status_code: int, detail: str, headers: dict | None) -> None:
        self.status_code = status_code
        self.detail = detail
        self.headers = headers
        super().__init__(status_code)