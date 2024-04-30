from pydantic_settings import BaseSettings
from pydantic import SecretStr


class AppSettings(BaseSettings):
    my_tokeb: SecretStr
    access_token: SecretStr
    user_id: str
    group_id: str


app_settings = AppSettings()
