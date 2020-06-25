# Basic container management
`docker ps` List running containers

`docker stop <CONTAINER ID>` Stop a container

`docker rm <CONTAINER ID>` Delete a container

`docker exec <CONTAINER ID> <CMD>` Run a command in a detached container

`docker logs -f <CONTAINER ID>` Get output of container

# Volumes
`docker volume create <VOLUME NAME>` Create volume

`-v <VOLUME NAME>:<MOUNT POINT>` Flag for `docker run`

`docker volume inspect <VOLUME NAME>` Get information about volume 
