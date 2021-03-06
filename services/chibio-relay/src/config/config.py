from typing import Optional

from pydantic import BaseSettings


class ForwarderConfig(BaseSettings):
    CACHE_KEY: str = "service.chibio-relay.forwarder"
    CHECK_INTERVAL: int = 10
    DATA_DIR: str = "data"
    DATA_GATEWAY_URL: str

    class Config:
        env_prefix = "FORWARDER_"


class ManagerConfig(BaseSettings):
    CACHE_KEY: str = "service.chibio-relay.manager"
    CHIBIO_SERVER_URL: str
    DEVICE_NAME: Optional[str]

    class Config:
        env_prefix = "MANAGER_"


class RedisCacheConfig(BaseSettings):
    URL: str = "redis://127.0.0.1:6379"

    class Config:
        env_prefix = "REDIS_CACHE_"


class RedisPubSubConfig(BaseSettings):
    URL: str = "redis://127.0.0.1:6389"

    class Config:
        env_prefix = "REDIS_PUBSUB_"


class ServerConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    class Config:
        env_prefix = "SERVER_"


class Config(BaseSettings):
    version: str = "ChiBio/v1alpha1"
    forwarder: ForwarderConfig = ForwarderConfig()
    manager: ManagerConfig = ManagerConfig()
    cache: RedisCacheConfig = RedisCacheConfig()
    pubsub: RedisPubSubConfig = RedisPubSubConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
