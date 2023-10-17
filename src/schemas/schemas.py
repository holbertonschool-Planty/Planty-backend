from pydantic import BaseModel


class CustomBadRequest(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class ErrorResponse(BaseModel):
    detail: str
    
class NotFoundResponse(ErrorResponse):
    pass

class BadRequestResponse(ErrorResponse):
    pass

class InternalServerErrorResponse(ErrorResponse):
    pass