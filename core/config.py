from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = 'sqlite+aiosqlite:///./bd.sqlite3'
    
    
settings = Setting()