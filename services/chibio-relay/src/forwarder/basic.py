import requests

from src.forwarder.payload import DataRow


class BasicForwarder:
    def __init__(self, cfg):
        super(BasicForwarder, self).__init__()

        self.data_gateway_url = cfg.DATA_GATEWAY_URL

    def forward(self, uuid, row: DataRow):
        # Forward the data to the service.date-gateway
        resp = requests.post(
            f"{self.data_gateway_url}/data",
            json={
                "uuid": uuid,
                "row": vars(row),
            },
        )
        resp.raise_for_status()
