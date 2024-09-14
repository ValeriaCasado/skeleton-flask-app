# Skeleton Flask App
To use as base for building services without having to re-do the basics.

Build the container image

TODO: auth module

`docker build -t test .`


Runs the container

`docker run -p 8000:8000 test`

## Container Ports vs. Host Ports
**Container Ports**: These are the ports that are exposed and used by the application inside the Docker container. Each container can have its own set of internal ports that applications inside the container listens on.

**Host Ports**: These are the ports on the host machine (the machine where Docker is running) that are mapped to the container's ports. By mapping a host port to a container port, you can access the application running inside the container from outside the Docker environment.


## Exposing ports

`EXPOSE`: In the Dockerfile, you use the EXPOSE instruction to indicate that the container will listen on a specific port.



`--publish`: Publishing Ports: To actually map the container port to a host port and make the service accessible from outside the container, you use the `-p` (or `--publish`) 



## Accessing Containers

From the Host: Use localhost or 127.0.0.1 if you’ve published ports from the container to the host.