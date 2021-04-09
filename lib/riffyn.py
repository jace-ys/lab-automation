import riffyn_nexus_sdk_v1 as riffyn


class Client:
    def default(api_key):
        configuration = riffyn.Configuration()
        configuration.api_key["api-key"] = api_key
        configuration.host = "https://api.app.riffyn.com/v1"
        return riffyn.ApiClient(configuration)
