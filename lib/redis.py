from redis import StrictRedis


class Client:
    def connect(url):
        return StrictRedis.from_url(url, decode_responses=True)
