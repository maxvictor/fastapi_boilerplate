import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    API_BASE_URL: str = os.getenv(
        "API_BASE_URL", "https://jsonplaceholder.typicode.com"
    )
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    RETRY_ATTEMPTS: int = int(os.getenv("RETRY_ATTEMPTS", 3))
    CIRCUIT_BREAKER_TIMEOUT: int = int(os.getenv("CIRCUIT_BREAKER_TIMEOUT", 30))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Boilerplate"


settings = Settings()
