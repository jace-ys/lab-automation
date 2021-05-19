# Development

## Minimum Requirements

These are the common requirements needed to get started with local development for most services:

- `GNU Make`
- `docker v1.13.0`
- `docker-compose v1.10.0`

These are mostly used to spin up containers containing auxiliary services that are depended upon by the service you're trying to develop. Some of these auxiliary services include the `db.redis` and `pubsub.redis` services.

On top of that, you will also need to meet the minimum requirements listed in each service's README.

## Running Locally

#### `external.chibio-server`
