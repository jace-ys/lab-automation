from pydantic import BaseSettings


class PluginConfig(BaseSettings):
    API_KEY: str
    CACHE_KEY: str = "service.control-tower.plugins.riffyn"
    POLL_INTERVAL: int = 10

    class Config:
        env_prefix = "PLUGINS_RIFFYN_"
