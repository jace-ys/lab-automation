import json
import redis
import uuid

publisher = redis.Redis(port=6389)
data = {
    "uuid": uuid.uuid4().hex[:16],
    "apiVersion": "ChiBio/v1alpha1",
    "protocol": "Bioreactor",
    "spec": {
        "chibio": {
            "devicePosition": "M0",
            "deviceName": "Hydrogen",
            "od": 0.42,
            "volume": 50,
            "thermostat": 40,
            "fp1Excite": "Laser",
            "fp1Gain": "128x",
        }
    },
    "metadata": {"source": {"name": "test", "spec": {}}},
}

publisher.publish("TecanSpark/v1alpha1", json.dumps(data))
