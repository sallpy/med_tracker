from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "postgresql+asyncpg://app_user:password123@localhost:5432/med_tracker_db"
    
    
settings = Setting()