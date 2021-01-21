from pydantic import BaseSettings


class PluginConfig(BaseSettings):
    API_KEY: str

    class Config:
        env_prefix = "PLUGIN_RIFFYN_"
