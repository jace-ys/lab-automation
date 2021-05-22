# Getting Started

This guide is a brief primer on how to get started with deploying and running the lab automation system in your lab environment.

At a high-level, the microservices that make up the overall system can be divided into core and edge services. See [Architecture](architecture.md) for an explanation of the differences between them.

This branch of the lab automation system is able to run all the core and edge services locally without any actual edge connections, allowing you to get a feel of how the system works. It does this by using mock implementations of the underlying device integrations. See [Local Mocks](development.md#local-mocks) for more info. To run the individual services for local development, check out their respective README's for instructions.

## Minimum Requirements

All services are designed to run on Unix-based operating systems such as Linux or MacOS, unless otherwise stated. Thus, most of the documentation is written with this in mind. Running them on a Windows machine might not produce the expected results.

#### Core Services

These are the main requirements needed to get started with running the core services:

- `docker v1.13.0`
- `docker-compose v1.10.0`

#### Edge Services

Edge services typically require you to run them individually on their respective machines - additional requirements for running these services are detailed in their respective READMEs.

The following are edge services:

- [`service.chibio-relay`](../services/chibio-relay)
- [`service.tecan-spark-relay`](../services/tecan-spark-relay)

## Quick Start

All the core services are packaged as [Docker](https://docs.docker.com/get-started/overview/) images and orchestrated using [Docker Compose](https://docs.docker.com/compose/). The Dockerfiles can be found under the [`docker`](../docker) directory.

The [`docker-compose.yaml`](../docker-compose.yaml) contains the configuration for the various containers. You might need to tweak it accordingly based on your own setup.

- To start all the services and auxiliary containers:

  ```
  docker-compose up
  ```

  Use the `-d` flag if you wish to run the containers in [detached mode](https://docs.docker.com/engine/reference/run/#detached--d).

- To rebuild the Docker images after making any changes to the code:

  ```
  docker-compose build
  ```

- To teardown the containers:

  ```
  docker-compose down -v
  ```

## Troubleshooting Deployments

To get the core and edge services connected and properly deployed, you might need to perform the following steps:

- Open host ports on your remote server running the core services. These ports can be found in the [`docker-compose.yaml`](../docker-compose.yaml) file.

- Use environment variables to point the edge services running on peripheral machines to the core services running on a remote server. Check each service's README for the list of environment variables that can be configured.

  For example, you might need to export the following environment variables before starting an edge service:

  ```
  export REDIS_CACHE_URL=redis://<IP address of your remote server>:6379
  export REDIS_PUBSUB_URL=redis://<IP address of your remote server>:6389
  ```
