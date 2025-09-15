from typing import Any
from pydantic import BaseModel


class HttpResponse(BaseModel):
    status_code: int
    body: Any = {}
    ok: bool
    message: str
