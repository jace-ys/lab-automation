# `service.control-tower`

The `service.control-tower` acts as the control plane of the routing layer. Its role is to publish [protocol triggers](../../docs/protocols.md) to the message queue such that downstream services can act on them. It uses a plugin-based system to integrate with various sources that can be used to generate protocol triggers.

## Minimum Requirements

- `python 3.9`
- `poetry 1.0`

## Usage

- Install dependencies:

  ```
  poetry install
  ```

- Start auxiliary containers:

  ```
  make dependencies
  ```

- Run the server:

  ```
  make
  ```

  Environment variables for the server that can be configured can be found in [`src/config/config.py`](src/config/config.py).

## How it Works

The `service.control-tower` uses plugins to watch for external events that can be used to generate a protocol trigger. It is able to watch multiple upstream sources for events and react accordingly, where the mapping logic of events to protocol triggers is handled by each individual plugin.

The core of any protocol trigger are the `apiVersion`, `protocol` and `spec` fields, so any plugin needs to have events that can modelled in this form. Protocol triggers are then published by the `service.control-tower` to the message queue, to be consumed by downstream services.

This "watching" behaviour can be as simple as watching for changes in a file, or as complex as watching an API for events. It can also be implemented in various ways - polling, webhooks, etc. It is up to the specific plugin to find the best implementation.

The `service.control-tower` also exposes a HTTP API for receiving protocol triggers via HTTP requests. This can be accessed by sending a protocol trigger as a JSON `POST` request to the `/triggers` endpoint.

## Plugins

The list of available plugins can be found under the [`plugins`](plugins) directory. Each plugin contains a README documenting usage and how it works.

Plugins might have additional configuration required. This can be set by prefixing environment variables with the following pattern:

```
PLUGIN_{PLUGIN_NAME}_
```

## Development

#### Adding New Plugins

Plugins will be automatically loaded from the `plugins` directory into the registry as long as they fulfil the `Watcher` interface defined in [`plugins/registry.py`](plugins/registry.py), and is contained within a file named `watcher.py`.

Essentially, an instance of this `Watcher` class will be instantiated for each plugin. The core logic for the plugin should be implemented in the `run` function, which will be called in separate threads. To publish a protocol trigger, each `Watcher` implementation needs to send a [`Trigger`](src/triggers/trigger.py) object to the `queue`:

```python
def run(self):
  # Logic for generating a Trigger object
  NotImplemented

  # Send the Trigger object to the queue
  self.queue.put(trigger)
```

See [`plugin.riffyn`](plugins/riffyn/watcher.py) for an example of how this is done.
