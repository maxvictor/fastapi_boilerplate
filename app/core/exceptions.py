from fastapi import HTTPException


class AppException(HTTPException):
    def __init__(self, status_code: int, code: str, description: str):
        self.code = code
        self.description = description
        super().__init__(status_code=status_code, detail=description)
