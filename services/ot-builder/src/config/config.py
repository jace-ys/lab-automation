from pydantic import BaseSettings


class RedisConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 6379

    class Config:
        env_prefix = "REDIS_"


class ServerConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    VIEWS_DIR: str = "src/views"

    class Config:
        env_prefix = "SERVER_"


class Config(BaseSettings):
    API_VERSION = "OT-2/v1alpha1"

    redis: RedisConfig = RedisConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
