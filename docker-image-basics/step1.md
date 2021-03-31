## Docker Image Commands

- List images in Docker.

`docker image ls`{{copy}}

- Download Docker image `ubuntu`.

`# Defaults to ubuntu:latest`
`docker image pull ubuntu`{{copy}}
`docker image ls`{{copy}}

- Run `ubuntu` as container with interactive shell open.

`docker run -it ubuntu`{{copy}}

- Display the `ubuntu` os info on the container Note that the release `20.04` of ubuntu. Then exit the container.

`cat /etc/os-release`{{copy}}
`exit`{{copy}}

- Download earlier version (`18.04`) of `ubuntu` image, which is tagged as `18.04` on Docker Hub.

`docker image pull ubuntu:18.04
docker image ls`{{copy}}

- Inspect `ubuntu` image and explain properties.

`# Defaults to ubuntu:latest`
`docker image inspect ubuntu`{{copy}}

`# Ubuntu with tag 18.04`
`docker image inspect ubuntu:18.04`{{copy}}

- Show the history of image `ubuntu` and pay attention to Docker image layers.

`docker image history ubuntu`{{copy}}

- Search for python Docker Images.
  
`docker search python`{{copy}}