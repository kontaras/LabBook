# Basic container management
`docker ps` List running containers

`docker stop <CONTAINER ID>` Stop a container

`docker rm <CONTAINER ID>` Delete a container

`docker exec <CONTAINER ID> <CMD>` Run a command in a detached container

`docker logs -f <CONTAINER ID>` Get output of container

# Run flags
`-i` Interactive  
`-t` TTY Session  
`-d` Detach (background)  
`-p <PORT>:<PORT>` Forward a port from the host to the container

# Volumes
`docker volume create <VOLUME NAME>` Create volume

`-v <VOLUME NAME>:<MOUNT POINT>` Flag for `docker run`

`docker volume inspect <VOLUME NAME>` Get information about volume 

# Garbage Collect
`docker image prune -a`
