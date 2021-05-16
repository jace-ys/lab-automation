# Architecture

The lab automation system is built as a set of microservices where the core services can run anywhere in the cloud, while peripheral services that may require access to hardware or a local file system are typically ran on the edge in conjunction with the equipment they are interfaced with. The services communicate over the network to enable data to flow between them.
