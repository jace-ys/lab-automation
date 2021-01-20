from pydantic import BaseSettings


class ForwarderConfig(BaseSettings):
    CACHE_KEY: str = "service.chibio-relay"
    CHECK_INTERVAL: int = 10
    DATA_DIR: str = "data"
    DATA_GATEWAY_ADDR: str

    class Config:
        env_prefix = "FORWARDER_"


class RedisCacheConfig(BaseSettings):
    CONNECTION_URL: str = "redis://127.0.0.1:6379"

    class Config:
        env_prefix = "REDIS_CACHE_"


class ServerConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    class Config:
        env_prefix = "SERVER_"


class Config(BaseSettings):
    forwarder: ForwarderConfig = ForwarderConfig()
    cache: RedisCacheConfig = RedisCacheConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
