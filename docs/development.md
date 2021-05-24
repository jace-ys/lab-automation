# Development

This is a quick guide on how you can get started with developing and extending ULAS. More in-depth documentation for each service can be found in their respective README's.

## Minimum Requirements

These are the common requirements needed to get started with local development for most services:

- `GNU Make`
- `docker v1.13.0`
- `docker-compose v1.10.0`

These are mostly used to spin up containers containing auxiliary services that are depended upon by the service you're trying to develop. Some of the common ones include the `db.redis` and `pubsub.redis` services.

On top of that, you will also need to meet the minimum requirements listed in each service's README.

## Simulating Protocol Triggers

To be able to conveniently test the behaviour of services in the service layer, a [small utility Python script](../protocols) is provided. This tool helps simulate protocol triggers that would typically be issued by the [`service.control-tower`](../services/control-tower), without having to run the server and its plugins.

## Local Mocks

To enable rapid prototyping without the need for hooking up ULAS to edge devices and actual hardware, mock implementations that imitate the behaviour of the underlying integrations are provided.

#### `external.chibio-server`

A mock Chi.Bio server is provided as a Docker image. With this mock implementation, you can start the server and interact with the Chi.Bio UI as you would for the actual server, but without any hardware side-effects - all the code for hardware interactions are commented out. The source code for this mock implementation can be found at https://github.com/jace-ys/ChiBio/tree/lab-automation.

You will first need to clone the above repository and build the Docker image:

```
docker build -t lab-automation/service.chibio-relay .
```

You can then start this container using the provided [`docker-compose.yaml`](../docker-compose.yaml):

```
docker-compose up
```

The Chi.Bio UI should be accessible at http://localhost:5000.

#### Mock SparkControl API

See [`service.tecan-spark-relay`](../services/tecan-spark-relay).
