from pydantic import BaseSettings


class PluginConfig(BaseSettings):
    API_KEY: str
    CACHE_KEY: str = "control-tower.plugins.riffyn"

    class Config:
        env_prefix = "PLUGINS_RIFFYN_"
