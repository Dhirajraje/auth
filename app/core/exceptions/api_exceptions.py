from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi.exceptions import HTTPException
from fastapi import status
from enum import Enum


class ErrorCodes(Enum):
    SOMETHING_WENT_WRONG='SOMETHING_WENT_WRONG'


class APIException(HTTPException):
    def __init__(self, status_code: int=status.HTTP_500_INTERNAL_SERVER_ERROR, error_code: str = ErrorCodes.SOMETHING_WENT_WRONG,error_message:str='Something went wrong!',details:Dict[str,Any]={}, headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, {
            'error_code':error_code,
            'error_message':error_message,
            'details':details
        }, headers)



