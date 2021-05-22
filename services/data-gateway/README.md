# `service.data-gateway`

The `service.data-gateway` acts as the data plane of the routing layer. Its role is to act as the gateway for data exported by downstream services in the service layer to upstream destinations for data storage - it uses a plugin-based approach to forward data to one or more upstream destinations.

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

The `service.data-gateway` exposes HTTP API endpoints that services can issue requests to with the data rows that they wish to forward. The API currently supports single and batch data rows. These data rows needs to be formatted as key-value pairs in JSON, where keys are expected to be camel-cased.

Examples of valid data objects:

```json
{
  "uuid": "uuid",
  "row": {
    "index": 0,
    "data": {
      "keyOne": 1,
      "keyTwo": "2",
      ...
    }
  }
}
```

```json
{
  "uuid": "uuid",
  "rows": [
    {
      "index": 0,
      "data": {
        "keyOne": 1,
        "keyTwo": "2",
        ...
      }
    }
  ]
}
```

The `index` key refers to the well index and is only required for [plate-based protocols](../../docs/protocols.md#platebased-protocols). As long as the request body conforms to the expected schema, it will be accepted and forwarded to each plugin's upstream destination; each plugin handles the actual logic for how to push data to their respective destinations.

## Plugins

The list of available plugins can be found under the [`plugins`](plugins) directory. Each plugin contains a README documenting usage and how it works.

Plugins might have additional configuration required. This can be set by prefixing environment variables with the following pattern:

```
PLUGIN_{PLUGIN_NAME}_
```

## Development

#### Adding New Plugins

Plugins will be automatically loaded from the `plugins` directory into the registry as long as they fulfil the `Pusher` interface defined in [`plugins/registry.py`](plugins/registry.py), and is contained within a file named `pusher.py`.

Some plugins might require some additional context to know how to forward data to upstream destinations. This can be achieved by using the trigger UUID to query the [`service.control-tower`](../control-tower) for metadata of the original trigger that is associated with the data - this information is available through the `/triggers/{uuid}` endpoint.

See [`plugin.riffyn`](plugins/riffyn/pusher.py) for an example of how this is done.
