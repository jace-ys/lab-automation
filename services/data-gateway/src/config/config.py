from pydantic import BaseSettings


class RedisCacheConfig(BaseSettings):
    ADDR: str = "127.0.0.1:6379"

    class Config:
        env_prefix = "REDIS_CACHE_"


class ServerConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    class Config:
        env_prefix = "SERVER_"


class Config(BaseSettings):
    cache: RedisCacheConfig = RedisCacheConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
