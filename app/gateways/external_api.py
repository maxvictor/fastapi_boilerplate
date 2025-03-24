import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from aiobreaker import CircuitBreaker
from app.core.config import settings
from app.core.exceptions import AppException

circuit_breaker = CircuitBreaker(
    fail_max=settings.RETRY_ATTEMPTS, timeout_duration=settings.CIRCUIT_BREAKER_TIMEOUT
)


@circuit_breaker
@retry(
    stop=stop_after_attempt(settings.RETRY_ATTEMPTS),
    wait=wait_exponential(multiplier=1, min=1, max=5),
)
def fetch_posts():
    try:
        response = requests.get(f"{settings.API_BASE_URL}/posts", timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise AppException(
            status_code=502,
            code="EXTERNAL_API_ERROR",
            description="Failed to fetch posts from external service",
        ) from e
