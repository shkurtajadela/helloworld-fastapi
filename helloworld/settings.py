from pydantic import BaseSettings


class Settings(BaseSettings):
    VERSION: str = '0.0.1'

    API_PREFIX: str = '/api/v1'
    API_TITLE: str = 'DataFusion Helloworld'

    DATABASE_URL: str = 'postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/helloworld'
    DATABASE_ECHO: bool = True

    ALLOWED_MIMETYPES: list[str] = [
        'text/csv',
        'text/plain',
    ]
    ALLOWED_EXTENSION: list[str] = [
        '.csv',
    ]

    LOGGING_FORMAT: str = '%(asctime)s %(levelname)s %(name)s %(message)s'
    LOGGING_LEVEL: str = 'INFO'


settings = Settings('.env')
