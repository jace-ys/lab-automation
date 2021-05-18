# Getting Started

This guide is a brief primer on how to get started with deploying and running the lab automation system in your lab environment.

At a high-level, the microservices that make up the overall system can be divided into core and edge services. See [Architecture](architecture.md) for an explanation of the differences between them.

To run the lab automation system locally and get a feel of how it works without any edge connections, see the guide on [Running Locally](development.md#running-locally).

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

All the core services are packaged as Docker images and orchestrated using Docker Compose. The Dockerfiles can be found under the [`docker`](../docker) directory.

- To start all the services and auxiliary containers:

  ```
  docker-compose up
  ```

- To rebuild the Docker images after making any changes to the code:

  ```
  docker-compose build
  ```

- To teardown the containers:

  ```
  docker-compose down -v
  ```
