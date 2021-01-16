from pydantic import BaseSettings


class ForwarderConfig(BaseSettings):
    BATCH_ENDPOINT: str
    CHECK_INTERVAL: int = 10
    DATA_DIR: str = "data"

    class Config:
        env_prefix = "FORWARDER_"


class RedisConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 6379

    class Config:
        env_prefix = "REDIS_"


class ServerConfig(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    class Config:
        env_prefix = "SERVER_"


class Config(BaseSettings):
    forwarder: ForwarderConfig = ForwarderConfig()
    redis: RedisConfig = RedisConfig()
    server: ServerConfig = ServerConfig()

    class Config:
        case_sensitive = True
