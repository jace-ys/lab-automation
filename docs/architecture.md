# Architecture

The lab automation system is built as a set of microservices where the core services can run anywhere in the cloud, while edge services that may require access to hardware or a local file system are typically ran on periphery machines in conjunction with the equipment they are interfaced with. All these services communicate over the network to enable the flow of data between them.

- External Layer
- Routing Layer
- Service Layer
- Device Layer
