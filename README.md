# Lab Automation Playground

As part of Jace's Final Year Project at Imperial College London, this is a playground repository for developing a distributed lab automation system. This is intended for use within the Imperial College Centre of Synthetic Biology.

## Architecture

#### [service.control-tower](services/control-tower)

#### [service.ot-builder](services/ot-builder)

## Development

#### Requirements

- `python v3.8+`
- `poetry v1.0+`
- `docker v19.03+`
- `docker-compose v1.25.5+`

#### Running Locally

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

## To-Do

- [ ] Use OpenAPI for defining protocol schemas
