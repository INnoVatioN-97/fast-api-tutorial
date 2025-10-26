import httpx
import asyncio
import random
from models import Campaign

async def send_campaign_to_external_api(campaign: Campaign) -> dict:
    """
    Simulates sending campaign data to an external API with exponential backoff retry.
    Uses https://httpbin.org/post to echo the data back.
    """
    max_retries = 3
    base_delay = 1.0  # seconds

    async with httpx.AsyncClient() as client:
        for attempt in range(max_retries):
            try:
                print(f"Attempt {attempt + 1} to call external API...")
                # 외부 API에 campaign 데이터를 JSON 형식으로 POST 요청을 보냅니다.
                # 테스트를 위해 URL을 "https://httpbin.org/status/503" 로 바꾸면 재시도 로직을 확인할 수 있습니다.
                response = await client.post("https://httpbin.org/post", json=campaign.dict(), timeout=10.0)
                response.raise_for_status()  # 4xx 또는 5xx 응답 코드가 오면 예외를 발생시킵니다.
                print("API call successful.")
                return response.json()
            except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                print(f"Attempt {attempt + 1} failed: {exc}")
                if attempt + 1 == max_retries:
                    print("Max retries reached. Giving up.")
                    return {"error": f"Failed to call external API after {max_retries} attempts: {exc}"}

                # Exponential backoff
                delay = (base_delay * (2 ** attempt)) + (random.uniform(0, 1))  # Add jitter
                print(f"Waiting for {delay:.2f} seconds before retrying...")
                await asyncio.sleep(delay)

    # This part should not be reached if max_retries > 0
    return {"error": "An unexpected error occurred in the retry loop."}
