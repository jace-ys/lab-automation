from pydantic import BaseSettings


class ForwarderConfig(BaseSettings):
    DATA_DIR: str = "data"
    FORWARD_ENDPOINT: str = "http://127.0.0.1:9000/data"
    CHECK_INTERVAL: int = 10

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
