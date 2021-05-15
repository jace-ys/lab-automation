from pydantic import BaseSettings


class ProtocolBuilderConfig(BaseSettings):
    CACHE_KEY: str = "service.ot-builder"

    class Config:
        env_prefix = "PROTOCOL_BUILDER_"


class RedisCacheConfig(BaseSettings):
    ADDR: str = "127.0.0.1:6379"

    class Config:
        env_prefix = "REDIS_CACHE_"


class RedisPubSubConfig(BaseSettings):
    ADDR: str = "127.0.0.1:6389"

    class Config:
        env_prefix = "REDIS_PUBSUB_"


class ServerConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    VIEWS_DIR: str = "src/views"

    class Config:
        env_prefix = "SERVER_"


class Config(BaseSettings):
    version: str = "OT-2/v1alpha1"
    builder: ProtocolBuilderConfig = ProtocolBuilderConfig()
    cache: RedisCacheConfig = RedisCacheConfig()
    pubsub: RedisPubSubConfig = RedisPubSubConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
