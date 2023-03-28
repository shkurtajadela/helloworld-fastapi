from typing import Any, Dict, Optional


class ServiceError(BaseException):
    detail: str
    extra: Optional[Dict[str, Any]]

    def __init__(
        self, detail: Optional[str] = None, extra: Optional[Dict[str, Any]] = None
    ) -> None:
        self.detail = detail or self.detail
        self.extra = extra


class InvalidMimetypeError(ServiceError):
    detail = 'Invalid file mimetype'