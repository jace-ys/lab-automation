from redis import StrictRedis


class Cache:
    def connect(connection_url):
        client = StrictRedis.from_url(connection_url, decode_responses=True)
        return client


class PubSub:
    def connect(connection_url):
        client = StrictRedis.from_url(connection_url, decode_responses=True)
        return client.pubsub()
