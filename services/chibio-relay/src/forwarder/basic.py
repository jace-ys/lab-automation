import requests

from src.forwarder.payload import DataRow


class BasicForwarder:
    def __init__(self, cfg):
        super(BasicForwarder, self).__init__()

        self.data_gateway_addr = cfg.DATA_GATEWAY_ADDR

    def forward(self, uuid, row: DataRow):
        resp = requests.post(
            f"http://{self.data_gateway_addr}/data",
            json={
                "uuid": uuid,
                "row": vars(row),
            },
        )
        resp.raise_for_status()
