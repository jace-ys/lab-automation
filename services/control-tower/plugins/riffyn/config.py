from pydantic import BaseSettings


class PluginConfig(BaseSettings):
    API_KEY: str
    CACHE_KEY: str = "service.control-tower.plugin.riffyn"
    POLL_INTERVAL: int = 10

    class Config:
        env_prefix = "PLUGIN_RIFFYN_"
