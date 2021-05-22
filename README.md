# Universal Lab Automation System for Synthetic Biology

## Foreword

This repository contains a distributed lab automation system built as part of Jace's final year project at Imperial College London. While it's primary use case is for research within the Imperial College Centre for Synthetic Biology, it also aims to be a customisable and extensible framework for others to adapt and develop automation within their own labs for a wide variety of use cases, even beyond the realms of biology and research.

This lab automation system is primarily meant as a low-cost and flexible alternative for small research labs in academia to empower their researchers through standardising and automating tasks that are often manual, repetitive and error-prone, with the ultimate goal of improving the reproducibility and efficiency of research. It also aims to tighten the closed-loop between experimental design, execution and results (in synthetic biology this is known as the [Design-Build-Test-Learn](https://miro.medium.com/max/1400/0*G8KtmhAB-6AscySL.jpg) cycle).

## Introduction

This lab automation system allows one to integrate various software and hardware components used within the lab into a unified platform that forms the backbone and "building blocks" that enables one to compose automated workflows and experimental protocols that span across multiple equipment and tools. These include [laboratory information management systems](https://en.wikipedia.org/wiki/Laboratory_information_management_system), [liquid handling robots](https://en.wikipedia.org/wiki/Liquid_handling_robot), [plate readers](https://en.wikipedia.org/wiki/Plate_reader), etc.

The system is built as a set of microservices that work in tandem by allowing these integrations to "communicate" with one another and facilitate the flow of data between them. To find out more about how the overall system works, check out the documentation on [Architecture](docs/architecture.md).

While this project is far from complete or production-ready, it demonstrates the proof of concept and lays the groundwork towards building a robust and universal platform for developing lab automation at scale.

## Services

The following is the list of services that make up the core of the lab automation system:

- [`service.control-tower`](services/control-tower)
- [`service.data-gateway`](services/data-gateway)
- [`service.ot-builder`](services/ot-builder)
- [`service.chibio-relay`](services/chibio-relay)
- [`service.tecan-spark-relay`](services/tecan-spark-relay)

Documentation on their purpose, how they work, as well as running and developing them individually can be found in each service's README. It is recommended to go through all of them before jumping into the [Getting Started](docs/getting-started.md) section on how to use the lab automation system.

Auxiliary services include (for their configuration, see [`docker-compose.yaml`](docker-compose.yaml)):

- `db.redis`
- `pubsub.redis`
- [`external.chibio-relay`](docs/development.md#external.chibio-server)

## Development

New integrations and features are very much welcome to further expand the capabilities and overall usefulness of the project. To extend or customise the lab automation system, check out the documentation on [Development](docs/development.md).

## Credits

I would like to thank the following people from the Imperial College Centre for Synthetic Biology for their support and advice throughout the project:

- Dr. Zoltan Tuza ([@zoltuz](https://github.com/zoltuz))
- Dr. Guy-Bart Stan
- Alice Boo
- Eszter Csibra
- Andreas Hadjimitsis
