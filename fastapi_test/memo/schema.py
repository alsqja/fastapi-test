from datetime import datetime
from pydantic import BaseModel


# Pydantic을 이용한 Type Hinting
class MemoCreate(BaseModel):
    regdate: datetime
    title: str
    body: str
