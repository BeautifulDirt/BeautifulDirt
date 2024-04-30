from pydantic_settings import BaseSettings
from pydantic import SecretStr


class AppSettings(BaseSettings):
    access_token: SecretStr
    user_id: str
    group_id: str


app_settings = AppSettings()
