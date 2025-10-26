from fastapi import Query

async def common_parameters(skip: int = 0, limit: int = Query(default=100, le=100)):
    """공통적으로 사용될 페이지네이션 파라미터를 처리하는 의존성 함수"""
    return {"skip": skip, "limit": limit}
