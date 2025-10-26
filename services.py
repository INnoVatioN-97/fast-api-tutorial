import httpx
from models import Campaign

async def send_campaign_to_external_api(campaign: Campaign) -> dict:
    """
    Simulates sending campaign data to an external API.
    Uses https://httpbin.org/post to echo the data back.
    """
    async with httpx.AsyncClient() as client:
        try:
            # 외부 API에 campaign 데이터를 JSON 형식으로 POST 요청을 보냅니다.
            response = await client.post("https://httpbin.org/post", json=campaign.dict(), timeout=10.0)
            response.raise_for_status()  # 4xx 또는 5xx 응답 코드가 오면 예외를 발생시킵니다.
            return response.json()
        except httpx.RequestError as exc:
            # 네트워크 오류 등 요청 중에 예외가 발생한 경우 처리합니다.
            return {"error": f"An error occurred while requesting {exc.request.url!r}: {exc}"}
