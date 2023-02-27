from databases.core import Database
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from fastapi.requests import Request

# Memo 스키마
from fastapi_test.memo.schema import MemoCreate

# Memo 모델
from fastapi_test.memo.model import memo

memo_router = APIRouter()


# 디비 쿼리를 위한 종속성 주입을 위한 함수
def get_db_conn(request: Request):
    return request.state.db_conn  # middleware 에서 삽입해준 db_conn


# 메모 생성
@memo_router.post("/memo")
async def memo_create(
    req: MemoCreate, db: Database = Depends(get_db_conn)  # 요청을 정의한 create 스키마에 맞게 전달 받음
):
    query = memo.insert()  # insert 쿼리 생성 (feat.sqlalchemy)

    # validation 처리가 필요할 듯
    values = {**req}
    try:
        await db.execute(query, values)  # 쿼리 실행 (feat.databases)
    except Exception as err:
        print(err)

    return {**req.dict}
