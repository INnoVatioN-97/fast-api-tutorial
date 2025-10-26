from fastapi import APIRouter, Depends
from models import Campaign
import services
from dependencies import common_parameters

router = APIRouter()


@router.get("/gateway")
def read_gateway():
    return {"message": "This is the gateway"}


@router.get("/gateway/campaigns")
async def list_campaigns(commons: dict = Depends(common_parameters)):
    # FastAPI가 common_parameters 함수를 실행하고, 그 결과를 commons 파라미터에 주입합니다.
    # 실제 앱에서는 이 값을 사용하여 데이터베이스를 쿼리합니다. (e.g., DB.get_items(skip=commons["skip"], limit=commons["limit"]))
    return {"message": "Listing campaigns with pagination", "params": commons}


# Pydantic 모델을 사용하는 POST 엔드포인트
@router.post("/gateway/campaigns")
async def create_campaign(campaign: Campaign):
    # 1. FastAPI가 요청 본문의 유효성을 검사합니다.
    # 2. 유효성 검사를 통과하면, 서비스 레이어의 함수를 호출합니다.
    external_api_response = await services.send_campaign_to_external_api(campaign)

    # 3. 외부 API의 응답을 클라이언트에게 반환합니다.
    return external_api_response
