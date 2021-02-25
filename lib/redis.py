from redis import StrictRedis


class Client:
    def connect(addr):
        return StrictRedis.from_url(f"redis://{addr}", decode_responses=True)
