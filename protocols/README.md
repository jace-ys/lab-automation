# Protocol Triggers Utility

This is a [small utility Python script](publisher.py) for simulating protocol triggers that would typically be issued by the [`service.control-tower`](../services/control-tower), without having to run the server and its plugins.

This script basically takes an input JSON file containing a protocol trigger and publishes it to a Redis instance, which downstream services can subscribe to and receive. This should make it more convenient to test the behaviour of a service upon receiving a protocol trigger.

## Usage

## Minimum Requirements

- `python 3.9`
- `poetry 1.0`

## Usage

- Install dependencies:

  ```
  poetry install
  ```

- Run the server:

  ```
  poetry run python publisher.py [path to file]
  ```

  You can configure the redis URL to publish to using the `--url` flag.

- Some example protocol triggers are contained in the [`examples`](examples) directory. You can simulate one of these protocol triggers like so:

  ```
  poetry run python publisher.py examples/ot-builder/plate-transfer.json
  ```
