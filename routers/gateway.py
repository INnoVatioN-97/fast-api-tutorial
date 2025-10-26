from fastapi import APIRouter
from models import Campaign
import services  # services.py 파일을 가져옵니다.

router = APIRouter()


@router.get("/gateway")
def read_gateway():
    return {"message": "This is the gateway"}


# Pydantic 모델을 사용하는 POST 엔드포인트
@router.post("/gateway/campaigns")
async def create_campaign(campaign: Campaign):
    # 1. FastAPI가 요청 본문의 유효성을 검사합니다.
    # 2. 유효성 검사를 통과하면, 서비스 레이어의 함수를 호출합니다.
    external_api_response = await services.send_campaign_to_external_api(campaign)

    # 3. 외부 API의 응답을 클라이언트에게 반환합니다.
    return external_api_response
