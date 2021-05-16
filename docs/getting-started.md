# Getting Started

## Requirements

- `python v3.8+`
- `poetry v1.0+`
- `docker v19.03+`
- `docker-compose v1.25.5+`

## Quick Start

All the services contain a Dockerfile for packaging them up into a single image.

To start all the services and auxiliary containers:

```
docker-compose up
```

To re-build the Docker images after making changes:

```
docker-compose build
```

To teardown the containers when you're done:

```
docker-compose down -v
```
