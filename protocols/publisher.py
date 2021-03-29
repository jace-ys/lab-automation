import json
import uuid

import redis
import click


@click.command("publish")
@click.argument("file")
@click.option(
    "--addr",
    help="Address of the redis server.",
    default="127.0.0.1:6389",
    show_default=True,
)
def publish(file, addr):
    with open(file, "r") as f:
        protocol = json.loads(f.read())
        data = {
            **protocol,
            **{
                "uuid": uuid.uuid4().hex[:16],
                "metadata": {
                    "source": {
                        "name": "test",
                        "spec": {
                            "experimentId": "123",
                            "runId": "abc",
                        },
                    }
                },
            },
        }

        publisher = redis.StrictRedis.from_url(f"redis://{addr}")
        publisher.publish(data["apiVersion"], json.dumps(data))


if __name__ == "__main__":
    publish()
