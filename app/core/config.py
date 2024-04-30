from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    access_token: str
    group_id: str
    user_id: str


app_settings = AppSettings()
