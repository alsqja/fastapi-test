from fastapi import FastAPI, Request
from fastapi_test.database import db_instance
from fastapi_test.memo.router import memo_router

app = FastAPI(title="Memo API", description="Memo CRUD API project", version="0.0.1")


@app.on_event("startup")
async def startup():
    await db_instance.connect()


@app.on_event("shutdown")
async def shutdown():
    await db_instance.disconnect()


@app.middleware("http")
async def state_insert(request: Request, call_next):
    request.state.db_conn = db_instance
    response = await call_next(request)
    return response


# 이 부분을 추가하여 router 구현로직을 적용
app.include_router(memo_router)
