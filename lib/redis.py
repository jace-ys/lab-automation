from redis import StrictRedis


class Client:
    def connect(connection_url):
        return StrictRedis.from_url(connection_url, decode_responses=True)
