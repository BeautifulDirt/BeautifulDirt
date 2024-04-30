from pydantic_settings import BaseSettings
from pydantic import SecretStr


class AppSettings(BaseSettings):
    access_token: SecretStr
    group_id: str
    user_id: str


app_settings = AppSettings()
