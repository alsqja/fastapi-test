# model.py

from datetime import datetime
from fastapi_test.database import db_engine, db_metadata
from sqlalchemy import Table, Column, String, Integer, DateTime

memo = Table(
    "memo",
    db_metadata,
    Column("idx", Integer, primary_key=True, autoincrement=True),
    Column("regdate", DateTime(timezone=True), nullable=False, default=datetime.now),
    Column("title", String(255), nullable=False),
    Column("body", String(2048), nullable=False),
)
# 테이블 정보로 테이블 생성한다
memo.metadata.create_all(db_engine)
