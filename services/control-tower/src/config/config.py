from pydantic import BaseSettings


class CommandPublisherConfig(BaseSettings):
    CACHE_KEY: str = "service.control-tower"

    class Config:
        env_prefix = "PUBLISHER_"


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
    publisher: CommandPublisherConfig = CommandPublisherConfig()
    cache: RedisCacheConfig = RedisCacheConfig()
    pubsub: RedisPubSubConfig = RedisPubSubConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
